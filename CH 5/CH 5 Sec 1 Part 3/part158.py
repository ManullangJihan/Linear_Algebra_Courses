#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:34:15 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[1,0,-2,2],
              [0,1,-1,1],
              [-1,0,0,2],
              [-1,0,-2,4]])
Eig_val = A.eigenvals() 
Eig_vec = A.eigenvects()
print(Eig_val)
print(Eig_vec)

# Second Method
import numpy as np
A = np.array([[1,0,-2,2],
              [0,1,-1,1],
              [-1,0,0,2],
              [-1,0,-2,4]])
Eig_val, Eig_vec = np.linalg.eig(A)
print(Eig_val)
print(Eig_vec)