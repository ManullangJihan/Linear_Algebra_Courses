#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:23:05 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[0,1,2],[1,2,-3],[-2,5,-2]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
B = np.array([r2,r1,r3])
r1 = B[0,:]
r2 = B[1,:]
r3 = B[2,:]
B = np.array([r1,r2,r3+2*r2])
r1 = B[0,:]
r2 = B[1,:]
r3 = B[2,:]
B = np.array([r1,r2,r3-9*r2])

det_A = np.linalg.det(A)
print('Determinant of A = ' + str(det_A))
print(B)