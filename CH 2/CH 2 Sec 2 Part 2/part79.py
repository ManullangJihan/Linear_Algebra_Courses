#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:42:42 2020

@author: hanjiya
"""

import numpy as np

M1 = np.array([[1,0],[1,1]])
M2 = np.array([[0,1],[1,1]])
M3 = np.array([[1,1],[0,1]])
M = np.array([[1,0],[3,2]])
A = np.array([[1,0,1,1],[0,1,1,0],[1,1,0,3],[1,1,1,2]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3-r1,r4-r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3-r2,r4-r2])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3*-1/2,r4])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3,r4+r3])

print(A)
print('is 2*M1+1*M2-1*M3 = M' + str(2*M1+1*M2-1*M3==M))

# Cara 2