#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:03:21 2020

@author: hanjiya
"""

import numpy as np
from scipy.linalg import orth

w1 = np.array([[1,1,0]]).T
w2 = np.array([[-1,1,0]]).T
w3 = np.array([[0,0,1]]).T
A = np.concatenate((w1,w2,w3),axis=1)
ans = orth(A)
# ans = np.linalg.qr(A)
print(ans)