#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:12:29 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,0,2,1],[2,1,5,5],[0,1,1,3]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A2 = np.array([r1,r2-2*r1,r3])
r1 = A2[0,:]
r2 = A2[1,:]
r3 = A2[2,:]
Af = np.array([r1,r2,r3-r2])

B = np.array([[1,0,2,1],[0,1,1,3],[0,0,0,0]])
r1 = B[0,:]
r2 = B[1,:]
r3 = B[2,:]
B2 = np.array([r1,r2,r3+r2])
r1 = B2[0,:]
r2 = B2[1,:]
r3 = B2[2,:]
Bf = np.array([r1,r3+2*r1,r3])

print(Af==B)
print(Bf==A)