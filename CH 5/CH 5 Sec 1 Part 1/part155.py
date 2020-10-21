#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:33:59 2020

@author: hanjiya
"""

from sympy import Matrix, Symbol
from sympy.solvers import solve

lamda = Symbol('lamda')
A = Matrix([[2,-1],[0,3]])
p = A.charpoly(lamda)
nilaiEigen = solve(p,lamda)
eig_val = A.eigenvals()
eig_vec = A.eigenvects()
print(nilaiEigen)
print(eig_val)
print(eig_vec)