#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:18:06 2020

@author: hanjiya
"""

from sympy import Matrix, symbols, zeros

x,y = symbols('x,y')
A = Matrix([[1,1],[2,-3],[0,5]])
T = zeros(3,2)
T = A @ Matrix([[x,y]]).T
print(T)
 