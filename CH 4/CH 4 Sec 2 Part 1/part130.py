#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:44:50 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[1,0,2,1],[2,1,5,5],[0,1,1,3]])
R,p = A.rref()
B = A[:,p]
print(B)