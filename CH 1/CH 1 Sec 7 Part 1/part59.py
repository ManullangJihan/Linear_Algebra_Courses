#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:06:42 2020

@author: hanjiya
"""

import numpy as np

E = np.eye(3)
E[2,:] = E[2,:] + 4*E[1,:]
F = np.eye(3)
F[2,:] = F[2,:] - 4*F[1,:]
print(np.dot(E,F))

# Cara Cepat
E = np.array([[1,0,0],[0,1,0],[0,4,1]])
invE = np.linalg.inv(E)
print(invE)