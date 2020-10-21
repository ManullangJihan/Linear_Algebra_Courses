#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:26:23 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[4,-5],[1,2]])
Eig_vec = A.eigenvects()
Eig_val = A.eigenvals()
print(Eig_vec)
print(Eig_val)