#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:41:20 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,1,0],
              [1,0,-1,0],
              [2,0,-2,0]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2-r1,r3-2*r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3-2*r2])
print(A)
