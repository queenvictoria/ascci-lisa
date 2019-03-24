#!/usr/bin/env python3

# ascii-lisa.py

"""
Stolen from Shanshan Wang.
https://wshanshan.github.io/python/asciiart/
"""

"""
@TODO

- [v] Read file.
- [ ] Select bit depth.
- [ ] Convert to ascci.
- [v] Resize file.
- [ ] Pass in some variables.
- [ ] Save it out.
- [ ] How many bits depth should I choose?
- [ ] How wide is the terminal? Fit to that.
- [ ] Ascii colour on the terminal.
"""

from PIL import Image
import numpy

# - [ ] Read file.
img = Image.open("bart.jpg")

# - [ ] Resize file.
img = img.resize((100, 100))

#Get the RGB color values of each pixel point and convert them to graycolor using the average method from numpy
# A bunch of pixels in a list.
# What base are these?
pixels = numpy.asarray(img)
pixels = numpy.sum(pixels, axis=2)

for row in pixels:
  for column in row:
    print (column, end='')
