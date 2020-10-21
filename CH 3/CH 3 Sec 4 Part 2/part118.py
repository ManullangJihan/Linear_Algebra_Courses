#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:35:39 2020

@author: hanjiya
"""

import numpy as np
from sympy import Matrix

b1 = np.array([[1,-1]]).T
b2 = np.array([[3,2]]).T
c1 = np.array([[1,2]]).T
c2 = np.array([[1,-2]]).T

# Part 1
A = np.concatenate((c1,c2,b1,b2),axis=1)
r1 = A[0,:]
r2 = A[1,:]
A = np.array([r1,r2-2*r1])
r1 = A[0,:]
r2 = A[1,:]
A = np.array([r1,-1/4*r2])
r1 = A[0,:]
r2 = A[1,:]
A = np.array([r1-r2,r2])
print(A)
PCB = A[:,[2,3]]
print(PCB)

# Part 2
A2 = np.concatenate((b1,b2,c1,c2),axis=1)
r1 = A2[0,:]
r2 = A2[1,:]
A2 = np.array([r1,r2+r1])
r1 = A[0,:]
r2 = A[1,:]
A2 = np.array([r1,1/5*r2])
r1 = A[0,:]
r2 = A[1,:]
A2 = np.array([r1-3*r2,r2])
print(A2)

# Part 3
Inv_PCB = np.linalg.inv(PCB)


# Cara Cepat
# Part 1
b1 = Matrix([[1,-1]]).T
b2 = Matrix([[3,2]]).T
c1 = Matrix([[1,2]]).T
c2 = Matrix([[1,-2]]).T
A = c1.col_insert(2,c2).col_insert(4,b1).col_insert(6,b2)
R, Apiv = A.rref()
PCB = R[:,[2,3]]

# Part 2
A2 = b1.col_insert(2,b2).col_insert(4,c1).col_insert(6,c2)
r2, A2piv = A2.rref()
PCB2 = r2[:,[2,3]]

# Part 3
Inv_PCB2 = PCB.inv()
print(Inv_PCB2)





