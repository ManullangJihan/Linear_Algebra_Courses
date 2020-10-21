#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:38:22 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,1,0],[2,-1,-2],[3,1,2]])
det_A = np.linalg.det(A)
invA = np.linalg.inv(A)
det_invA = np.linalg.det(invA)

print('Determinant of A = ' + str(det_A))
print('Determinant of Inverse A = ' + str(det_invA))

