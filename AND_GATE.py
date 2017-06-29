#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:00:02 2017

@author: lenalee
"""
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = (x1*w1) + (x2*w1)
    
    if tmp <= theta:
        return 0
    elif tmp >= theta:
        return 1
