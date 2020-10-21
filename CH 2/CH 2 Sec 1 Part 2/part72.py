#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:17:26 2020

@author: hanjiya
"""

import numpy as np

u = np.array([[1,2,3,0]]).T
v = np.array([[-3,2,-1,4]]).T
w = np.array([[-1,-1,5,-1]]).T
result = 2*u + 3*v - 4*w
print(result)