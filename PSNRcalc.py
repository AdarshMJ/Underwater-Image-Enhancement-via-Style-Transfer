#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:25:21 2018

@author: adarsh
"""

import numpy 
import math
import cv2

original = cv2.imread("/Users/adarsh/Desktop/res/5b/30.png")
contrast = cv2.imread("/Users/adarsh/Desktop/res/5b/18248239138.png")
def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

d=psnr(original,contrast)
print(d)
