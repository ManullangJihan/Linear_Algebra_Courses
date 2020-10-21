#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:15:38 2020

@author: hanjiya
"""

import numpy as np

u = 2* np.array([[-1],[2],[3]])
v = 3* np.array([[2],[-3],[1]])
u_plus_v = u + v
print(u_plus_v)