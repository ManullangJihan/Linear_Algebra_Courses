#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:24:38 2020

@author: hanjiya
"""

import numpy as np
import math

A = np.array([[1,2,3,-3],[2,2,-1,0],[1,4,2,3],[-2,-3,2,4]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
B = np.array([r1,r3,r2,r4])
det_A = math.ceil(np.linalg.det(A))
det_B = math.floor(np.linalg.det(B))
print(det_A)
print(det_B)
print('is Det A equal to Det B ?' +str(det_A==det_B))
print('is Det A equal to Absolute value Det B ?' +str(det_A==np.abs(det_B)))