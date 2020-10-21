#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:02:22 2020

@author: hanjiya
"""

from sympy import Matrix, nsimplify

w1 = Matrix([[1,1,1]]).T
A = w1.T
orthogonal_basis = nsimplify(A, rational=True).nullspace()
print(orthogonal_basis)