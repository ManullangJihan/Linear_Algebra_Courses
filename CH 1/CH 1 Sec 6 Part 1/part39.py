#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:00:19 2020

@author: hanjiya
"""

import numpy as np
import math

A = np.array([[1,2,3,5],[0,5,6,7],[0,0,3,-2],[0,0,0,2]])
det_A = np.linalg.det(A)
det_A = math.floor(det_A)
print(det_A)