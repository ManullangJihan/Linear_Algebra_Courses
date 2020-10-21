#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:52:24 2020

@author: hanjiya
"""

from sympy import Matrix, diag

P = Matrix([[1,3,1],[2,-2,1],[-1,2,2]])
det_p = P.det()
D = diag(1,2,-3)
A = P @ D @ P.inv()
Q = Matrix([[1,2,1],[0,1,1],[1,1,1]])
det_Q = Q.det()
B = Q @ A @ Q.inv()
R, S = B.diagonalize()
print(B==R@S@R.inv())