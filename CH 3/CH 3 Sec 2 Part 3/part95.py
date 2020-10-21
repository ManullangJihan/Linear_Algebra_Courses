#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:01:41 2020

@author: hanjiya
"""

from sympy import *
import numpy as np

c1,c2,c3,x = symbols('c1,c2,c3,x')
p1 = 1+2*x-x**2
p2 = 1+x
p3 = 1-x+2*x**2

A = np.array([[1,1,1,2],[2,1,-1,4],[-1,0,2,1]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2-2*r1,r3+r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3+r2])
print(A)
