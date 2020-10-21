#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:23:26 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[1,1],[1,3]])
Eig_val = A.eigenvals()
Eig_vect = A.eigenvects()
print(Eig_val)
print(Eig_vect)