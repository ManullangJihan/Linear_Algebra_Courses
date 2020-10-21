#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:02:55 2020

@author: hanjiya
"""

import numpy as np

u = np.array([[1,2,3]]).T
v = np.array([[1,2,1]]).T
print(u.T @ v)