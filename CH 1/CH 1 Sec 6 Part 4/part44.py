#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:19:40 2020

@author: hanjiya
"""

import numpy as np
A = np.array([[1,2,-3],[2,5,1],[-1,3,4]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2-2*r1,r3+r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A1 = np.array([r1,r2,r3-5*r2])
det_A = np.linalg.det(A)
det_A_final = np.linalg.det(A1)
print(det_A)
print(det_A_final)