#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:27:36 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[-3,-1,5],[-2,1,2],[-2,-1,4]])
P = A.eigenvects()
D = A.eigenvals()
print(P)
print(D)