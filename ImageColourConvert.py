#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:21:35 2020

@author: aaronwright
"""

from PIL import Image
from transforms import RGBTransform # from source code mentioned above
import itertools

# Open image for duplication
im = Image.open("/Users/aaronwright/Documents/DataScience/Projects/Photomosaics/Images/Hiro.jpg").convert("RGB")

# Save down variety of different RGB values 
lis = [x for x in range(0, 256, 25)]
perm = list(itertools.permutations(lis, 3))

name = 1
for x in perm:
    count = .25
    for j in range(0, 3):
        new = RGBTransform().mix_with(x,factor=count).applied_to(im)  
        new.save("/Users/aaronwright/Documents/DataScience/Projects/Photomosaics/Hiro/hiro"+str(name)+".jpg", "JPEG", optimize=True, )
        count += .25
        name += 1
