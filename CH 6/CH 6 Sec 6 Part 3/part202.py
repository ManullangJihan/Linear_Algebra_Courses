#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:32:27 2020

@author: hanjiya
"""

from sympy import Matrix, Symbol, factor, eye

## Orthogonally Diagonalize the Matrix
lamda = Symbol('lamda')
A = Matrix([[1,2,2],[2,1,2],[2,2,1]])
p = A.charpoly(lamda)
print(factor(p,lamda))
# factor(p,lamda)
# = [ lambda - 5, lambda + 1, lambda + 1]

b = A - 5*eye(3)
print(b)
c = A - (-1)*eye(3)
print(c)
V = A.eigenvects()
D = A.egenvals()
v1 = V[:,0]
v2 = V[:,1]
v3 = V[:,2]
print(v1 @ v2)
print(v1 @ v3)
print(v2 @ v3)
w1 = v1.copy()
w2 = v2.copy()
w3 = v3 - (v3 @ w2) / (w2 @ w2) @ w2
w3 = w3*2
W = v1.col_insert(1,w2).col_insert(2,w3)
WWT = W.T @ W
Q = Matrix([w1/])
