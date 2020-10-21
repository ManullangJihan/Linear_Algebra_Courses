#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 07:22:30 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[-3,4],[5,-2]])
det_A = np.linalg.det(A)

print(det_A)