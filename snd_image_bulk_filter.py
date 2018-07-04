#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 03:27:01 2018

@author: github.com/sahandv
"""
from __future__ import print_function
import cv2
import os
import numpy as np

def snd_image_filter(image, kernel_div = None):
    img_w = image.shape[0]
    img_h = image.shape[1]
    block_w = img_w
    block_h = img_h
    if kernel_div is None:
        return image

    kernel = np.ones((int(block_w/kernel_div),int(block_h/kernel_div)),np.float32)/((block_w*block_h)/250)
    filtered = cv2.filter2D(image,-1,kernel)

    return filtered

IMAGE_DIR = "input_dir"
OUTPUT_DIR = "output_dir"

file_names = next(os.walk(IMAGE_DIR))[2]
for i in range(len(file_names)):
    image = cv2.imread(os.path.join(IMAGE_DIR,file_names[i]))
    image_new = snd_image_filter(image, 15)
    cv2.imwrite(os.path.join(OUTPUT_DIR,file_names[i]),image_new)

