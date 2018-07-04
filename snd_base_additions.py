#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 17:51:25 2018

@author: github.com/sahandv
"""
from __future__ import print_function, division

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

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

# =============================================================================
# Get actual and predicted Y values and return percentage of accuracy for each 
# class.
# =============================================================================
def class_accuracy_percentage_calc(Y_actual,Y_prediction):
    df_confusion = pd.crosstab(Y_actual, Y_prediction, rownames=['Actual'], colnames=['Predicted'], margins=True)
    count_of_classess = df_confusion.All.size
    class_accuracy_percentage = []
    for i in range(count_of_classess-1):
        class_accuracy_percentage.append(float(df_confusion[i][i])/float(df_confusion.All[i]))
    return class_accuracy_percentage
