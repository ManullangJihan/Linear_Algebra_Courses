#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:56:36 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.proj3d import proj_transform
from mpl_toolkits.mplot3d.axes3d import Axes3D
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

plt.rcParams['figure.figsize'] = [20,17]
plt.rcParams.update({'font.size':18})

## Code Problem Start Here
u1 = np.array([[1,-1,1]]).T
u2 = np.array([[0,1,1]]).T
u3 = np.array([[-2,-1,1]]).T
A = np.dot(u1.T,u2)
B = np.dot(u1.T,u3)
C = np.dot(u2.T,u3)
print(A==0)
print(B==0)
print(C==0)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.arrow3D(0,0,0,
           u1[0,0],u1[1,0],u1[2,0],
           mutation_scale=20,
           LineWidth=1,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           u2[0,0],u2[1,0],u2[2,0],
           mutation_scale=20,
           LineWidth=1,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           u3[0,0],u3[1,0],u3[2,0],
           mutation_scale=20,
           LineWidth=1,
           arrowstyle="-|>")
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
ax.set_zlim(0,1.2)

plt.grid('on')
plt.show()
















