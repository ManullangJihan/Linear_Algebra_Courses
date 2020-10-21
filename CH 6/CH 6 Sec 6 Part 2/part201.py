#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:27:52 2020

@author: hanjiya
"""

from sympy import Matrix, Symbol

lamda = Symbol('lamda')
A = Matrix([[0,4,2],[4,0,2],[2,2,2]])
p = A.charpoly(lamda)
print(p)

# cp = solve(p==0,lambda)
# v1 = A - cp(1)*eye(3);
# v2 = A - cp(2)*eye(3);
# v3 = A - cp(3)*eye(3);

