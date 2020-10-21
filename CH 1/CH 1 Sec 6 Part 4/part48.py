#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:33:48 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,-1],[3,1,2],[-1,2,1]])
B = np.array([[1,1,1],[2,5,-3],[2,0,1]])
C = np.linalg.det(np.dot(A,B))
D = np.dot(np.linalg.det(A),np.linalg.det(B))

print(C)
print(D)
