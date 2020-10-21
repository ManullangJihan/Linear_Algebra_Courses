#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:14:19 2020

@author: hanjiya
"""

import numpy as np
import scipy
import scipy.linalg

A = np.array([[2,1],[6,-2]])
b = np.array([[4],[12]])
r1 = A[0,:]
r2 = A[1,:]
U = np.array([r1,r2-3*r1])
L = np.array([[1,0],[3,1]])

Aproof = L @ U
y,resid,rank,s = np.linalg.lstsq(L,b)
x,residx,rankx,sx = np.linalg.lstsq(U,y)

print(Aproof)
print(y)
print(x)

# Cara kedua
A2 = np.array([[2,1],[6,-2]])
b2 = np.array([[4],[12]])
P2,L2,U2 = scipy.linalg.lu(A2)
Aproof2 = L2 @ U2
y2,resid,rank,s = np.linalg.lstsq(L2,b2)
x2,resid,rank,s = np.linalg.lstsq(U2,y2)

print(Aproof2)
print(y2)
print(x2)

