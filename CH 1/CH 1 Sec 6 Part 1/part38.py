#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 07:56:42 2020

@author: hanjiya
"""

import numpy as np
import math

A = np.array([[1,2,3],[-1,2,1],[2,1,1]])
det_A = np.linalg.det(A)
det_A = math.ceil(det_A)
print('Determinant of A = ' + str(det_A))