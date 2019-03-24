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
- [ ] Resize file.
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

#Get the RGB color values of each pixel point and convert them to graycolor using the average method from numpy
# A bunch of pixels in a list.
pixels = numpy.asarray(img)
print(pixels.size)
pixels = numpy.sum(pixels, axis=2)

print(pixels)
print(pixels.size)
print(pixels.size * 3)
