# Photomosaics

This is a semi-guided project. See link:
https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/

This script allows you to generate a photomosaic. This is an image made up of hundreds/thousands of smaller images.

# Instructions

### ImageColourConvert.py

The `ImageColourConvert.py` file will generate multiple images of differing RGB values from the same image. This is useful if you want all the smaller images in your mosaic to be the same image.

Be careful when changing values here, as it could result in thousands of images!!

This file borrows from `transforms.py` which is not my own code.

### Photomosaics.py

Here you'll want to update `STEP`, `main_image`, and `small_images`. 

* `STEP` will dictate the number of pixels across/down for each square section created on the main image. You may need to play around with this a bit
* `main_image` is the path to your main image
* 'small_images` is the path to your small images

Not that script may take a little while to run, depending on how many small images you have.

# What I learned from this project

I learned a great deal about image handling in Python using `PIL`. I gained some knowledge of RGB colours and how these relate to pictures/images.

I also improved my skill working with raw Python and programming skills, with looping being a major part of this project. 

Some of the logic used in this project did take a great deal of thinking!

# What I can improve

* Script can be very slow depending on how many small images it has. The way I've done it may not be all that efficient
* There are techniques I'm aware of that can blur the edges of small images and make the mosaic look a little more natural
