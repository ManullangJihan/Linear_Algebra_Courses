#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:03:34 2020

@author: hanjiya
"""

import numpy as np

A = np.random.randint(low=5,high=16,size=(6,6))
B = np.tril(A, k=0)
diag_A = np.diag(A)
C = np.prod(np.diag(B))
det_B = np.linalg.det(B)

print(A)
print(B)
print(diag_A)
print(C)
print(det_B)