#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:11:46 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2],[-1,4]])
E = np.eye(2)
E1 = np.array([E[0,:], E[0,:]+E[1,:]])
E2 = np.array([E[0,:], 1/6*E[1,:]])
E3 = np.array([E[0,:]-2*E[1,:], E[1,:]])
print(E3 @ E2 @ E1 @A)

C = np.linalg.inv(E1) @ np.linalg.inv(E2) @ np.linalg.inv(E3)
print(C)