#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:29:12 2020

@author: hanjiya
"""

from sympy import Matrix, diag

A = Matrix([[3,-8,14],[2,-5,10],[1,-2,4]])
P, D = A.diagonalize()
print(A@P)
print(P@D)
print(A@P == P@D)
print(A == P*D*P.inv())

P = Matrix([[P[:,0],P[:,1],P[:,2]]])
D = diag(-1,1,2)
print(A@P)
print(P@D)
print(A@P == P@D)
print(A == P*D*P.inv())