#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:24:57 2020

@author: hanjiya
"""

from sympy import Symbol

x = Symbol('x')
f = 2*x + 3

finv = (x-3)/2

print(f.subs(x,5))
print(finv.subs(x,13))
print(f.subs(x,finv.subs(x,13)))

