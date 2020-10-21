#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:04:10 2020

@author: hanjiya
"""

import numpy as np

u = np.array([[1],
              [2],
              [5]])
v = np.array([[-1],
              [2],
              [-1]])
w = np.array([[4],
              [5],
              [2]])
c = -2
property_1 = np.dot(u.T,v) == np.dot(v.T,u)
property_2 = np.dot(u.T,v+w) == np.dot(u.T,v)+np.dot(u.T,w)
property_3 = c*np.dot(u.T,v) == np.dot(u.T,c*v)
print(property_1)
print(property_2)
print(property_3)