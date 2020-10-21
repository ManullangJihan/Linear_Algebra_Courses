#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:40:55 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,1,-2],[2,1,2],[3,4,2]])
At = A.T
det_A = np.linalg.det(A)
det_At = np.linalg.det(At)

print('Determinant of A = ' + str(det_A))
print('Determinant of A transpose = ' + str(det_At))

