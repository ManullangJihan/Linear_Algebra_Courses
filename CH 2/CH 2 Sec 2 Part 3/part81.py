#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:54:12 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,-1],[3,2,-2],[-1,-1,4]])
b = np.array([[1,2,3]]).T
print(A@b)

