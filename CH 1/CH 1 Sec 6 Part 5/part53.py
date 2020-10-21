#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:16:10 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,1],[2,-1,-1],[1,1,2]])
b = np.array([[0],[2],[6]])

A1 = A.copy()
A2 = A.copy()
A3 = A.copy()

A1[:,0] = b[:,0]
A2[:,1] = b[:,0]
A3[:,2] = b[:,0]

detA = np.linalg.det(A)
detA1 = np.linalg.det(A1)
detA2 = np.linalg.det(A2)
detA3 = np.linalg.det(A3)

x1 = detA1/detA
x2 = detA2/detA
x3 = detA3/detA

print(x1)
print(x2)
print(x3)