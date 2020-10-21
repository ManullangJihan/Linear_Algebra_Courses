#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:09:06 2020

@author: hanjiya
"""

from sympy import Matrix, nsimplify

A = Matrix([[1,2,-1,0,1,1,1],
            [1,1,1,2,3,5,1],
            [0,0,2,2,2,4,0],
            [1,1,1,2,3,5,0],
            [1,1,1,2,3,5,1]])
n = 7 # size(A,2)
BN = nsimplify(A, rational=True).nullspace()
nullityA = 3 # Size(BN,2)
rankA = A.rank()

print(rankA + nullityA == n)