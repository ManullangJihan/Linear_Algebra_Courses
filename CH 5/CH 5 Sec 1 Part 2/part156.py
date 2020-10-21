#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:03:57 2020

@author: hanjiya
"""

from sympy import Matrix, Symbol, expand, factor
import numpy as np
import matplotlib.pyplot as plt

#
lamda = Symbol('lamda')
A = Matrix([[1,0,0],[1,0,1],[2,-2,3]])
p = A.charpoly(lamda)
eigA = A.eigenvals()
print(expand((lamda-1)**2*(lamda-2)))
print(factor(p))
print(eigA)

#
plt.rcParams['figure.figsize'] = [20,18]
plt.rcParams.update({'font.size':18})
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-2,2,20)
t = np.linspace(-2,2,20)
S,T = np.meshgrid(s,t)
X = S-T
Y = S
Z = T
ax.plot_surface(X,Y,Z,EdgeColor='g',alpha=0.1)
ax.arrow3D(0,0,0,1,1,0,LineWidth=2, Color='r', mutation_scale=20, arrowstyle="-|>")
ax.arrow3D(0,0,0,-1,0,1,LineWidth=2, Color='r', mutation_scale=20, arrowstyle="-|>")
plt.grid('on')
plt.show()

#
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-2,2,20)
x = np.zeros_like(s)
y = (1/2)*s
z = s
ax.plot(x,y,z,LineWidth=2,Color='b')
ax.arrow3D(0,0,0,0,1/2,1,LineWidth=5,Color='r',mutation_scale=20, arrowstyle="-|>")
ax.plot(0,0,0,'o',Color='r')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-2,2)
plt.grid('on')
plt.show()

