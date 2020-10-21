#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:30:05 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[0,1,-2,4],[2,-2,4,6],[0,1,1,1],[0,2,3,5]])
det_A = np.linalg.det(A)
B = np.array([[1,-1,2,3],[0,1,-2,4],[0,1,1,1],[0,2,3,5]])
B = B[1:5,1:5]
r1 = B[0,:]
r2 = B[1,:]
r3 = B[2,:]
B = np.array([r1,r2-r1,r3-2*r1])
det_B = np.linalg.det(B)*-2

print('Determinant of A = ' + str(det_A))
print(det_B)