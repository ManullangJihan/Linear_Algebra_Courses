#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:20:55 2020

@author: hanjiya
"""

import numpy as np
import math

A = np.array([[1,-3,4],[2,0,-2],[3,-4,4]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
B = np.array([r1,3*r2,r3])
C = np.linalg.det(A)*3
det_B = np.linalg.det(B)

print(math.ceil(C))
print(math.ceil(det_B))