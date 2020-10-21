#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:24:30 2020

@author: hanjiya
"""

import numpy as np
from sympy import Matrix

C = np.array([[1,2,1],
              [1,1,0],
              [2,1,1]])
B = np.array([[1,0,0],
              [1,1,1],
              [0,1,0]])
A = np.concatenate((C,B),axis=1)
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2-r1,r3-2*r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,-1*r2,r3])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3+3*r2])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,1/2*r3])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1-r3,r2-r3,r3])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1-2*r2,r2,r3])
print(A)
PCB = A[:,[3,4,5]]
v = np.array([[1,-1,2]]).T
V = PCB @ v
print(V)

# Cara Cepat
C = Matrix([[1,2,1],
              [1,1,0],
              [2,1,1]])
B = Matrix([[1,0,0],
              [1,1,1],
              [0,1,0]])
A = C.col_insert(3,B)
R, piv = A.rref()
PCB = R[:,[3,4,5]]
v = Matrix([[1,-1,2]]).T
V2 = PCB * v
print(V2)