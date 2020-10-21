#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:47:29 2020

@author: hanjiya
"""

from sympy import Matrix, nsimplify

# Entry matrix A in Matlab
A = Matrix([[1,2,3,1,5],
            [1,0,1,0,3],
            [0,1,1,1,1],
            [1,-1,0,2,2]])

# Determine the size of matrix A
print(A.shape)

# Determine the column size of A
n = 5 #A.shape[0,1]

#find a basis for the null space
BN = nsimplify(A, rational=True).nullspace()
print(BN)

# Create a basis for the column space
nullityA = 2 # BN.shape[1]

# Check the basis for the column space of A
R,P = A.rref()

# Create these vectors from the matrix A
print(A[:,P])

# Check the basis for the column space of A
rankA = A.rank()

# Finally show that column rank(A) + nullity(A) = n
print(rankA + nullityA == n)