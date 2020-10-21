#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:35:57 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,3,-1],[2,0,-1,-1],[1,2,1,-1],[2,2,-3,4]])
det_2A = np.linalg.det(2*A)
print('Determinant of 2*A = ' + str(det_2A))

det_2A = 2**4 * np.linalg.det(A)
print('Determinant of 2*A = ' + str(det_2A))