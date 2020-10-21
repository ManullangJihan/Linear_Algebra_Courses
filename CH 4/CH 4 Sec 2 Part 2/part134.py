#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:17:56 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [24,16]
plt.rcParams.update({'font.size' : 30})

# Part 1
A = np.array([[1,2,8,4],
              [-1,1,1,2],
              [1,2,8,1]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2+r1,r3-r1])
print(A)

# Part 2
B = np.array([[1,2,8],
              [-1,1,1],
              [1,2,8]])
r1 = B[0,:]
r2 = B[1,:]
r3 = B[2,:]
Bfinal = np.array([r1,r2+r1,r3-r1])
BT = B[:,0:2]
print(BT)

# Visualize Part 2
A = np.array([[1,2,8],
              [-1,1,1],
              [1,2,8]])
P = 1 - 2*np.random.rand(3,100)
Pts = A @ P
s = np.linspace(-4,4,11)
t = np.linspace(-4,4,11)
S,T = np.meshgrid(s,t)
X = S + 2*T
Y = -S + T
Z = S + 2*T
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,Color='green',alpha=0.1)
ax.scatter3D(Pts[0,:], Pts[1,:], Pts[2,:], Color='b')

plt.show()