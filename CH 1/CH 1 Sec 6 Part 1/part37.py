#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 07:53:45 2020

@author: hanjiya
"""

import numpy as np
import math

A = np.array([[1,2,-1],[2,1,-3],[4,-5,1]])
M11 = A[1:3,1:3]
C11 = (-1)**(1+1)*np.linalg.det(M11)
M12 = A[0:3:2,0:2]
C23 = (-1)**(2+3)*np.linalg.det(M11)
print(math.floor(C11))
print(math.floor(C23))