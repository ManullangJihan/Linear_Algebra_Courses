#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:41:34 2020

@author: hanjiya
"""

from sympy import Matrix, zeros

A1 = Matrix([[1,1,1],[1,0,2],[0,1,1]])
A = A1.col_insert(3, zeros(3,1))
Aref,piv = A.rref()
print(Aref)