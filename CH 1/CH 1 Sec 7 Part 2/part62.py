#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:15:18 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[4,4,4],[4,3,3],[1,1,4]])
E = np.eye(3)
E1 = np.array([E[0,:], E[1,:]-E[0,:], E[2,:]])
E2 = np.array([E[0,:], E[1,:], E[2,:]-1/4*E[0,:]])
U = E2 @ E1 @ A
L = np.linalg.inv(E1) @ np.linalg.inv(E2)
A = np.dot(L,U)
print(U)
print(L)
print(A)