#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:07:13 2020

@author: hanjiya
"""

from sympy import *
import numpy as np

c1,c2,c3,c4,a,b,c,d = symbols('c1,c2,c3,c4,a,b,c,d')
u = Matrix([[1,1],[1,0]])
v = Matrix([[0,1],[1,1]])
w = Matrix([[1,0],[1,1]])
x = Matrix([[1,1],[0,1]])
M = Matrix([[a,b],[c,d]])


A = np.array([[1,0,1,1,a],
              [1,1,0,1,b],
              [1,1,1,0,c],
              [0,1,1,1,d]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2-r1,r3-r1,r4])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3-r2,r4-r2])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3,r4-2*r3])
print(A)