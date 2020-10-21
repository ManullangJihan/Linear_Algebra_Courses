#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:32:41 2020

@author: hanjiya
"""

import numpy as np
import scipy
import scipy.linalg

A = np.array([[-1,-2,1],[-3,0,-2],[3,-3,1]])
b = np.array([[1],[1],[1]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
U = np.array([r1,r2-3*r1,r3+3*r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
U = np.array([r1,r2,r3+3/2*r2])
L = np.array([[1,0,0],[3,1,0],[-3,-3/2,1]])
Aproof = L @ U
y,resid,rank,s = np.linalg.lstsq(L,b)
Lproof = y * b
x,resid,rank,s = np.linalg.lstsq(U,y)
Uproof = x * y

print(Aproof)
print(y)
print(Lproof)
print(x)
print(Uproof)

# Cara 2
A = np.array([[-1,-2,1],[-3,0,2],[3,-3,1]])
b = np.array([[1],[1],[1]])
P,L,U = scipy.linalg.lu(A)
b = P @ b
y,resid,rank,s = np.linalg.lstsq(L,b)
x,resid,rank,s = np.linalg.lstsq(U,y)

print(b)
print(y)
print(x)