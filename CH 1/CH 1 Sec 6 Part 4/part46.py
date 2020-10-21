#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:26:50 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[2,4,6],[-3,-1,4],[-2,1,2]])
det_A = np.linalg.det(A)
B = np.array([[1,2,3],[-3,-1,4],[-2,1,2]])
r1 = B[0,:]
r2 = B[1,:]
r3 = B[2,:]
B = np.array([r1,r2+3*r1,r3+2*r1])
r1 = B[0,:]
r2 = B[1,:]
r3 = B[2,:]
B = np.array([r1,r2,r3-r2])
det_B = np.linalg.det(B) * 2

print('Determinant of A is ' + str(det_A))
print('Determinant of B is ' + str(det_B))
