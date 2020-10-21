#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:05:05 2020

@author: hanjiya
"""

import numpy as np

B = np.eye(3)
B[2,:] = B[2,:] - 7*B[0,:]
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(B@A)