#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:23:06 2020

@author: hanjiya
"""

from sympy import Matrix, Symbol, factor, zeros,eye

lamda = Symbol('lamda')
A = Matrix([[0,1,0],[0,0,1],[2,-5,4]])
p = A.charpoly(lamda)
print(p)
print(factor(p))
# solve(p == 0,lambda)

# Eigenvectors Corresponding of lambda = 1
A1_1 = A - 1* eye(3)
A1_2 = zeros(3,1)
A1 = A1_1.col_insert(3,A1_2)
Eig_vec1, p = A1.rref()
print(Eig_vec1)

# Eigenvectors Corresponding of lambda = 2
A2_1 = A - 2* eye(3)
A2_2 = zeros(3,1)
A2 = A2_1.col_insert(3,A2_2)
Eig_vec2, p = A2.rref()
print(Eig_vec2)

# Cara Cepat
Eig_vec = A.eigenvects()
Eig_val = A.eigenvals()
print(Eig_vec)
print(Eig_val)

