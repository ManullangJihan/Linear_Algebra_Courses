#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 07:38:12 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,3],[-2,0,4],[-2,-2,3]])
M12 = A[1:3,0:3:2]
det_M12 = np.linalg.det(M12)
print(det_M12)
M33 = A[0:2,0:2]
det_M33 = np.linalg.det(M33)
print(det_M33)