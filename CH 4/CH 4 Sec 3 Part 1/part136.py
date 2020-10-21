#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:33:40 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[1,2],[2,4]])
null_A = A.nullspace()
print(null_A)
