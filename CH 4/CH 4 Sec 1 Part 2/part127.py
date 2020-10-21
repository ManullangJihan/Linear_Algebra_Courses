#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:05:54 2020

@author: hanjiya
"""

from sympy import symbols, Matrix, zeros

x,y = symbols('x,y')
A = Matrix([[2,3],[-5,3]])
T = zeros(2,2)
T = A @ Matrix([[x,y]]).T
print(T[0,0])
print(T[1,0])
