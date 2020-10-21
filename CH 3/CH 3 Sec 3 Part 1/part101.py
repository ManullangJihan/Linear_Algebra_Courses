#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:49:01 2020

@author: hanjiya
"""

from sympy import *
import numpy as np

a,b,c,d,c1,c2,c3,c4 = symbols('a,b,c,d,c1,c2,c3,c4')
M1 = Matrix([[1,0],[2,1]])
M2 = Matrix([[2,1],[0,1]])
M3 = Matrix([[0,1],[2,1]])
M4 = Matrix([[2,1],[1,0]])
M = Matrix([[a,b],[c,d]])
eqns = c1*M1+c2*M2+c3*M3+c4*M4
print(eqns)

A = np.array([[1,2,0,2,a],
              [0,1,1,1,b],
              [2,0,2,1,c],
              [1,1,1,0,d]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3-2*r1,r4-r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3+4*r2,r4+r2])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3,r4-1/3*r3])
print(A)