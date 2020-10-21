#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:19:25 2020

@author: hanjiya
"""

import numpy as np
from scipy.linalg import orth

# Cara Pertama
A = np.array([[1,-2],[2,1]])
a1 = A[:,0]
a2 = A[:,1]
q1 = a1 / np.linalg.norm(a1)
q2 = a2 / np.linalg.norm(a2)
Q = np.concatenate((q1,q2),axis=0)
print(Q)

# Cara kedua
Q_cara2 = orth(A)
print(Q_cara2)