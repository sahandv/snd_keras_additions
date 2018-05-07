#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 17:51:25 2018

@author: github.com/sahandv
"""
from sklearn.model_selection import train_test_split

# =============================================================================
# Split / Partition data with easy to understand proportions for your network 
# to 3 part.
# =============================================================================
def snd_data_split_3(X,Y,train_proportion,test_proportion,validation_proportion):
    size_1 = 1 - train_proportion
    size_2 = validation_proportion/(test_proportion+validation_proportion)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=size_1)
    x_test, x_valid, y_test, y_valid = train_test_split(x_test, y_test, test_size=size_2)
    return x_train,x_test,x_valid,y_train,y_test,y_valid

