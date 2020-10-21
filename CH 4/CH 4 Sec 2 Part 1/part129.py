#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:24:19 2020

@author: hanjiya
"""

from sympy import Matrix, zeros, nsimplify, GramSchmidt

A = Matrix([[1,0,2,1],[2,1,5,5],[0,1,1,3]])
B = A.col_insert(4, zeros(3,1))
RM, Bpiv = B.rref()

Ans = A.nullspace()
Ans = GramSchmidt(Ans,True)
n1 = Ans[0]
norm_n1 = n1.norm()
print(norm_n1)

n2 = Ans[1]
norm_n2 = n2.norm()
print(norm_n2)

RM = nsimplify(A, rational=True).nullspace()
print(RM)
