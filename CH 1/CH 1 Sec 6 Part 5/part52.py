#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:42:55 2020

@author: hanjiya
"""

import numpy as np

A = np.matrix([[2,3,-2],[3,1,0],[-3,-3,3]])
adjA = A.getH()
invA = np.linalg.inv(A)
invA = 1 / np.linalg.det(A) @ adjA

print(invA)