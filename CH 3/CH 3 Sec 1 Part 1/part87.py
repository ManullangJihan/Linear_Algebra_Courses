#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:27:11 2020

@author: hanjiya
"""

import numpy as np
from sympy import *

A = np.array([[0,3,-4],[-3,0,5],[4,-5,0]])
min_A = -A
transpose_A = A.T
skew_mat = transpose_A == min_A
print(skew_mat)

c = Symbol('c')
cA = c*transpose_A
minus_cA = -c*A
skew_mat2 = cA == minus_cA
print(skew_mat2)

