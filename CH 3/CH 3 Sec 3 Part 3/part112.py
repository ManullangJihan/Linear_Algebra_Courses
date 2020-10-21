#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:43:40 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[1,3,2],[1,1,0],[-1,0,1]])
B, piv = A.rref()
print(B)