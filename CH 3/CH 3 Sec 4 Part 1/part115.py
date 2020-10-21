#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:48:23 2020

@author: hanjiya
"""

from sympy import Matrix

A = Matrix([[1,-3,2,-1],
            [1,1,1,1]])
Btransition, piv = A.ref()
print(Btransition)