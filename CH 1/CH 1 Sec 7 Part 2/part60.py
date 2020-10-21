#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:09:56 2020

@author: hanjiya
"""

import numpy as np

L = np.array([[1,0,0],[2,2,0],[4,4,4]])
inv_L = np.linalg.inv(L)
print(inv_L)