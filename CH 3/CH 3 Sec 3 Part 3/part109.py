#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:27:14 2020

@author: hanjiya
"""

import numpy as np

A = np.matrix([[1,2,3],[-2,-1,-3],[3,-1,0]])
det_A = np.linalg.det(A)
print(det_A)