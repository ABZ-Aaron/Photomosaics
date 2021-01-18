#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:22:58 2020

@author: aaronwright

Purpose: Build a photomosaic

Glossary:
    
    Main Image = Background image for photomosaic
    Small Images = Images which make up photomosaic
    
"""

# Import relevant libraries
from PIL import Image
import glob
import math

################### Functions ######################

# Function which takes main image as input and returns square of pixels
def divide_into_square(step, pixels, x, y):
    row = pixels[y:y + step]
    square = []
    for z in row:
        square.append(z[x:x + step])
    return square

# Function which takes square or small image and returns the average RGB value
def convert_to_RGB(image):
     r = 0; g = 0; b = 0
     count = 0
     for row in image:
         for tup in row:
             r += tup[0]; g += tup[1]; b += tup[2]
             count += 1           
     r = int(r / count); g = int(g / count); b = int(b / count) 
     return r, g, b

# Function which checks a square's average RGB value, and identifies the closest
# RGB value in list of small images
def closest_match(square_rgb, small_image_dict):
    minimum = 1000
    matched_image = ""
    for i, (k, v) in enumerate(small_image_dict.items()):
        redParam = (v[0]-square_rgb[0])**2
        greenParam = (v[1]-square_rgb[1])**2
        blueParam = (v[2]-square_rgb[2])**2
        dist = math.sqrt( redParam + greenParam + blueParam ) 
        if dist < minimum:
            minimum = dist
            matched_image = k
    return matched_image

# Function to open images and resize.
def open_image(image, width, height):
    try:
        im = Image.open(image).convert("RGB")
        im = im.resize((width,height))
    except:
        print(f"Image {image} not imported successfully")
    
    return im

# Function to open small images, calculate average RGB value, and 
# save data to dictionary.
def save_down_small_images(small_imgs): 
    small_image_dict = {}
    count = 0
    for filename in glob.glob(small_imgs+'*jpg'):
        im = Image.open(filename).convert("RGB")
        small_pixels = [list(im.getdata())]
        r, g, b = convert_to_RGB(small_pixels)
        small_image_dict[filename] = (r, g, b)
        count += 1
    return small_image_dict
    
################### Script ######################

# Set the number of pixels across/down for each square
STEP = 70

# Specify directories for main image and smaller images.
main_image = "/Users/aaronwright/Documents/DataScience/Projects/Photomosaics/Images/Rebecca1.jpg"
small_images = "/Users/aaronwright/Documents/DataScience/Projects/Photomosaics/Akira/"

# Import the main image, and save data down for small images.
img = open_image(main_image, 6000, 4000)
imgs = save_down_small_images(small_images)

# Generate list of pixels of main image and divide based on width and height of imported image.
pixels = list(img.getdata())
pixels = [pixels[p:p+img.width] for p in range(0, len(pixels), img.width)] 

# Generate blank image to output photomosaic
output_img = Image.new('RGB', (img.width, img.height))

# Loop through pixel matrix of main image, with each iteration representing a square of pixels.
for x in range(0, len(pixels[0])-1, STEP):
    for y in range(0, len(pixels)-1, STEP):  
        # Generate square of pixels and find average RGB value for square.
        square = divide_into_square(STEP, pixels, x, y)
        r, g, b = convert_to_RGB(square)
        # Find small image that closely matches current square's RGB value.
        small_image = closest_match((r, g, b), imgs) 
        # Open small Image, and paste it into output image at current coordinates.
        small_image = open_image(small_image, STEP, STEP) 
        output_img.paste(small_image, (x, y))
        
        
# Output Image
output_img.show()


    
    
    









