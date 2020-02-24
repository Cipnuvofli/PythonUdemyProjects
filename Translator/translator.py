# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:10:46 2020

@author: Joseph
"""

from translate import Translator

translator = Translator('ja');
originalText = open('TestText.txt', 'r', encoding="utf-8");
result = open('result.txt', 'w', encoding="utf-8");


for line in originalText:
    translated = translator.translate(line);
    result.write(translated);




originalText.close();
result.close();