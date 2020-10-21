#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:57:26 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[3,-1,-1],[0,1,0],[1,-1,1]])
V = A.eigenvects()
D = A.eigenvals()
print(V)
print(D)