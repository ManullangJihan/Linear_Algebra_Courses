#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:18:12 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[-1,2,-4],[-1,-4,-4],[-3,-2,3]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2-r1,r3-3*r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
U = np.array([r1,r2,r3-4/3*r2])

E = np.eye(3)
E1 = np.array([E[0,:], E[1,:]-E[0,:], E[2,:]])
E2 = np.array([E[0,:],E[1,:],E[2,:]-3*E[0,:]])
E3 = np.array([E[0,:],E[1,:],E[2,:]-4/3*E[1,:]])
L = np.linalg.inv(E1) @ np.linalg.inv(E2) @ np.linalg.inv(E3)
A = L @ U

print(L)
print(A)