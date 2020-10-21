#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:05:54 2020

@author: hanjiya
"""

from sympy import *

A = Matrix([[1,3,1,7],
            [1,4,2,11],
            [0,1,1,4],
            [1,3,1,7]])
A_rref, piv = A.rref()
print(A_rref)