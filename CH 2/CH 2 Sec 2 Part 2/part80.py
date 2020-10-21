#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:49:45 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,1,4],[2,1,-1,5],[-1,-1,-1,-2],[1,1,-4,7]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2-2*r1,r3+r1,r4-r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,-1/3*r2,r3,r4])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3-r2,r4+r2])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,-1*r3,r4])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
r4 = A[3,:]
A = np.array([r1,r2,r3,r4+4*r3])
print(A)

# Cara 2
