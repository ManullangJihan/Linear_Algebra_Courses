#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:29:44 2020

@author: hanjiya
"""

from sympy import Matrix, symbols

# Part 1 : Determine the Determinant
A = Matrix([[1,3],[1,4]])
det_A = A.det()
print(det_A)

# Part 2 Determine the Inverse
Ainv = A.inv()
print(Ainv)

# Part 3 Proof the Theorem
x,y = symbols('x,y')
s = Matrix([[x,y]]).T
T = A @ s
Tinv = Ainv @ s

print(T.subs([(x,x),(y,y)]))
print(Tinv.subs([(x,x),(y,y)]))
