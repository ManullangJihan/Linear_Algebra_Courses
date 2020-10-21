#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 06:44:50 2020

@author: hanjiya
"""

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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

a,b,c = symbols('a,b,c')
A = np.array([[1,1,0,a],[0,1,1,b],[1,0,1,c]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3-r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3+r2])
print(A)

v = np.array([[1,0,1]]).T
u = np.array([[1,1,0]]).T
w = np.array([[0,1,1]]).T
A = np.array([v,u,w]).T
v = 2 * np.random.rand(3,100) - 1
vecs = A @ v
vecs = np.reshape(vecs,(3,100))
fig = plt.figure()
ax = fig.gca(projection='3d')
for k in range(0,100):
    ax.arrow3D(0,0,0,vecs[0,k],vecs[1,k],vecs[2,k],LineWidth=1,arrowstyle="-|>")
ax.set_ylim3d(-2,2)
ax.set_xlim3d(-2,2)
ax.set_zlim3d(-2,2)
plt.grid('on')
det_A = np.linalg.det(A)
print(det_A)