#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:32:47 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,-3,4],[4,0,-2,1],[1,1,-1,1],[1,3,-2,-4]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
B = np.array([r1,r2-4*r1,r3,r4])
C = np.array([r1,r2+4*r1,r3,r4])

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_C = np.linalg.det(C)

print(det_A)
print(det_B)
print(det_C)
print('det A, det B and det C equal? ' + str(det_A == det_B == det_C))