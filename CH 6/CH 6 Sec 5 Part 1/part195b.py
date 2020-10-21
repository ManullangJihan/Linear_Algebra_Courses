#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:50:01 2020

@author: hanjiya
"""

import numpy as np
A = np.array([[2,1],[1,2],[0,0]])
b = np.array([[4,4,2]]).T
w = np.array([[4,4,0]]).T
V = 1 - 2*np.random.rand(2,10)
U = A @ V
B = b - U
print(np.linalg.norm(B,axis=0))
print(np.linalg.norm(B[:,1]))
X = 0.1 - 0.2*np.random.rand(2,10)
X = np.concatenate((X,np.zeros((1,10))),axis=0)
u = w + X
print(np.linalg.norm(b-u,axis=0))