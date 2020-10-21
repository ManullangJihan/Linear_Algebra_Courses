#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:56:15 2020

@author: hanjiya
"""

import numpy as np

A = np.array([[1,2,3],[2,1,0]])
B = np.array([[1,0],[1,1],[2,-1]])
ans1 = A @ B
ans2 = np.array([np.dot(A,B[:,0]), np.dot(A,B[:,1])]).T
print('isequal ans1 = ans2' + str(ans1==ans2))
