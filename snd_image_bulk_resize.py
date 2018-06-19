#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 03:27:01 2018

@author: github.com/sahandv
"""
from __future__ import print_function
import cv2
import os

def snd_image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):

    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized

IMAGE_DIR = "/home/sahand/Desktop/Baidu"
OUTPUT_DIR = "/home/sahand/Desktop/Baidu-s-alt"
file_names = next(os.walk(IMAGE_DIR))[2]
for i in range(len(file_names)):
    image = cv2.imread(os.path.join(IMAGE_DIR,file_names[i]))
    image = snd_image_resize(image, width = 800, height = None, inter = cv2.INTER_AREA)
    cv2.imwrite(os.path.join(OUTPUT_DIR,file_names[i]),image)