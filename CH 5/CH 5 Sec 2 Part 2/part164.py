#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:59:59 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[2,-2,2],[0,0,2],[0,2,0]])
P,D = A.diagonalize()
print(A@P)
print(P@D)
print(A@P == P@D)