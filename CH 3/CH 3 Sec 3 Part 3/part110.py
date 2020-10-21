#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:27:52 2020

@author: hanjiya
"""

from sympy import Matrix,eye

A = Matrix([[1,3],[-1,1],[2,1],[4,2]])
M = A.col_insert(3,eye(4))
B, piv = M.rref()
A_final = M[:,[0,1,2,4]]
det_Afinal = A_final.det()
print(B)
print(A_final)
print(det_Afinal)
