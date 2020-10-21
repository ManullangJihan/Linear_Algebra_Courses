#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:55:21 2020

@author: hanjiya
"""

from sympy import *
import numpy as np

c1,c2,c3,a0,a1,a2,x = symbols('c1,c2,c3,a0,a1,a2,x')
p1 = x+2
p2 = x**2 + 1
p3 = x**2 - 1
p = a0 + a1*x +a2*x**2

A = np.array([[2,1,0,a0],
              [1,0,-1,a1],
              [0,1,1,a2]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2-1/2*r1,r3])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3+2*r2])
print(A)