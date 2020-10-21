#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:54:54 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.eye(3)
B[:,[0,1]] = B[:,[1,0]]
print(np.dot(B,A))