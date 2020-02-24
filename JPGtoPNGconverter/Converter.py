# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:16:28 2020

@author: Joseph
"""

import sys
import os
from PIL import Image

#grab first and second argument as directories
#save jpg files in original first directory as pngs in second directory, make the second directory if it doesn't exist
#loop through folder 1, convert images to PNG, save them in new folder

jpegDirectory = sys.argv[1];
pngDirectory = sys.argv[2];
jpegContents = os.listdir(jpegDirectory);
counter = 0;
for picture in jpegContents:
        base = Image.open(f"{jpegDirectory}/{picture}");
        filename = picture.split(".");
        if os.path.isdir(pngDirectory):
            base.save(f"{pngDirectory}/{filename[0]}.png", "PNG")
            counter+=1
        else:
            os.mkdir(pngDirectory)
            base.save(f"{pngDirectory}/{filename[0]}.png", "PNG")
            counter+=1
        

    