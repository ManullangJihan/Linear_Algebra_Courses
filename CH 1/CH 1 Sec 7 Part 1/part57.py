#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:03:31 2020

@author: hanjiya
"""

import numpy as np

B = np.eye(3)
B[1,:] = 2*B[1,:]
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.dot(B,A))