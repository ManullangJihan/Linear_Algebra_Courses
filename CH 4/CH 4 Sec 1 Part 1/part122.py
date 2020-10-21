#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:02:40 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,-1,-2],[2,1,2]])
u = np.array([[1,2,5]]).T
A_times_u = A @ u
print(A_times_u)