#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:06:08 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *

v1 = np.array([[1,2,-1]]).T
v2 = np.array([[2,2,1]]).T
v3 = np.array([[1,1,1]]).T
b = np.array([[2,0,2]]).T
A = np.array([[1,2,1,2],[2,2,1,0],[-1,1,1,2]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2-2*r1,r3+r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3+3/2*r2])
ans1 = -2*v1+4*v2+(-4*v3)
print('isequal b = -2*v1+4*v2+(-4*v3)' + str(b==ans1))

# Fast Method
A = Matrix([[1,2,1,2],[2,2,1,0],[-1,1,1,2]])
A_rref_matrix, pivot = A.rref()
print(A_rref_matrix)

# Visualize Our Answer
s = np.linspace(-1.5,1.5,20)
t = np.linspace(-1.5,1.5,20)
S,T = np.meshgrid(s,t)
X = S+2*T
Y = -2*S+T
Z = S+2*T
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,Color='g')

from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.patches import FancyArrowPatch
class Arrow3D(FancyArrowPatch):
    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._xyz = (x,y,z)
        self._dxdydz = (dx,dy,dz)

    def draw(self, renderer):
        x1,y1,z1 = self._xyz
        dx,dy,dz = self._dxdydz
        x2,y2,z2 = (x1+dx,y1+dy,z1+dz)

        xs, ys, zs = proj_transform((x1,x2),(y1,y2),(z1,z2), renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        super().draw(renderer)
        
def _arrow3D(ax, x, y, z, dx, dy, dz, *args, **kwargs):
    '''Add an 3d arrow to an `Axes3D` instance.'''

    arrow = Arrow3D(x, y, z, dx, dy, dz, *args, **kwargs)
    ax.add_artist(arrow)
setattr(Axes3D,'arrow3D',_arrow3D)

ax.arrow3D(0,0,0,1,-2,1,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,2,1,2,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,-1,2,3,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")

plt.show()
