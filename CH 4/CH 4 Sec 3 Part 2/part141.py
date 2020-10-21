#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:23:05 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[2,3,1,2],
            [1,3,2,4],
            [3,3,3,3],
            [2,1,3,4]])
det_A = A.det()
print(det_A)