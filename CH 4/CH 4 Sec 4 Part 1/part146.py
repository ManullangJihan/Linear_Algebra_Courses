#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:36:04 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[1,1],[1,-1],[0,1]])
b1 = Matrix([[1,1]]).T
b2 = Matrix([[2,1]]).T
c1 = Matrix([[1,1,1]]).T
c2 = Matrix([[1,1,0]]).T
c3 = Matrix([[1,0,0]]).T
T1 = A @ b1
T2 = A @ b2
print(T1)
print(T2)

T = c1.col_insert(1,c2).col_insert(2,c3).col_insert(3,T1).col_insert(4,T2)
M, p = T.rref()
TCB = M[:,[3,4]]
print(TCB)

v = Matrix([[2,-3]]).T
T2 = b1.col_insert(1,b2).col_insert(2,v)
M2, m2p = T2.rref()
vB = M2[:,2]
print(vB)

TVC = TCB @ vB
TV = c1.col_insert(1,c2).col_insert(2,c3)
TV = TV @ TVC
print(TV)