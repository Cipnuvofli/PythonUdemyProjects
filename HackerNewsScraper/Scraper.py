# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:01:46 2020

@author: Joseph
"""

import requests
from bs4 import BeautifulSoup
import pprint

#Takes the desired number of pages of Hacker News and generates a 2 dimensional array of their links and subtext
def prepare_links_and_subtext(pages):
    
    mega_links = [];
    mega_subtext = [];
    
    for i in range(1, pages+1):
        res = requests.get('https://news.ycombinator.com/news?p='+str(i))
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        mega_links = mega_links+links;
        mega_subtext = mega_subtext+subtext;
    return [mega_links, mega_subtext]
        
#Sorts the stories with the highest voted one on top
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse = True )
    
#Goes through the 2d array made by the preparation function(idx in preparationFunction[0][idx] and preparationFunction[1][idx] refer to different parts of the same item
#If a story has more than 100 points, it gets fed to the list of items to feed to the sorter    
def  create_custom_hn(preparationFunction):
    hn = []
    for idx, item in enumerate(preparationFunction[0]):
        title = preparationFunction[0][idx].getText()
        href =  preparationFunction[0][idx].get('href', None)
        vote = preparationFunction[1][idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


print(create_custom_hn(prepare_links_and_subtext(2)))