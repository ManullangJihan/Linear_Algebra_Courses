#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:52:59 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,3,4],[2,4,6],[-1,1,2]])
det_A = np.linalg.det(A)
print(det_A)

A = np.array([[1,3,4,0],[2,4,6,0],[-1,1,2,0]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2-2*r1,r3+r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3+2*r2])
print(A)
