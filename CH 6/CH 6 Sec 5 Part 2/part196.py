#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:08:04 2020

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

## Code Start Here
plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

A = np.array([[1,-1],
              [1,1],
              [2,1]])
b = np.array([[2,1,1]]).T
x = np.linalg.inv(A.T @ A) @ A.T @ b
w1 = A @ x
w2 = b - w1

## Visualize Our Answer
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = S-T
Y = S+T
Z = 2*S+T
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
for i in(b,w1):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0], LineWidth=1,
               Color='b',mutation_scale=20,
               arrowstyle="-|>")

ax.arrow3D(w1[0,0],w1[1,0],w1[2,0],
           w2[0,0],w2[1,0],w2[2,0], LineWidth=1,
           Color='b', mutation_scale=20,
           arrowstyle="-|>")

ax.text(0.5*b[0,0],0.5*b[1,0],0.5*b[2,0],'b',FontSize=12,BackgroundColor='w')
ax.text(0.5*w1[0,0],0.5*w1[1,0],0.5*w1[2,0],'w_1',FontSize=12,BackgroundColor='w')
ax.text(w1[0,0]+0.5*w2[0,0],w1[1,0]+0.5*w2[1,0],w1[2,0]+0.5*w2[2,0],
        'w_2',FontSize=12,BackgroundColor='w')

ax.set_xlim(-0.5,2.5)
ax.set_ylim(-2,2)
ax.set_xlim(-1,2)

plt.grid('on')
plt.show()






















