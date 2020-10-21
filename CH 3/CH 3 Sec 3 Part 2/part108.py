#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:07:34 2020

@author: hanjiya
"""

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

A = Matrix([[1,-1,1],
            [2,13,1],
            [-1,1,1]])
B, piv = A.rref()
print(B)

fig = plt.figure()
ax = fig.gca(projection='3d')

s = np.linspace(-2.5,2.5,20)
t = np.linspace(-2.5,2.5,20)
S,T = np.meshgrid(s,t)
X = S-T
Y = 2*S + 13*T
Z = -S + T
ax.plot_surface(X,Y,Z,FaceColor='g',EdgeColor='none',antialiased=False,alpha=0.5)
X2 = S.copy()
Y2 = T.copy()
Z2 = np.zeros_like(S)
ax.plot_surface(X2,Y2,Z2,FaceColor='r',EdgeColor='none',antialiased=False,alpha=0.5)
ax.set_xlim3d(-20,20)
ax.set_ylim3d(-20,20)
ax.set_zlim3d(-10,10)

plt.show()