#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:19:02 2020

@author: hanjiya
"""

import numpy as np
from scipy.linalg import null_space
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

fig = plt.figure()
ax = fig.gca(projection='3d')

s = np.linspace(-2,2,20)
t = np.linspace(-2,2,20)
S,T = np.meshgrid(s,t)
X = S-T
Y = S+T
Z = S+T
ax.plot_surface(X,Y,Z,Color='g',EdgeColor='none',alpha=0.1)
ax.arrow3D(0,0,0,
           1,1,1,
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           -1,1,1,
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
plt.grid('on')
plt.show()

## 2
fig = plt.figure()
ax = fig.gca(projection='3d')

w1 = np.array([[1,1,1]]).T
w2 = np.array([[-1,1,1]]).T
A = np.concatenate((w1,w2),axis=1)
ans = null_space(A)
s = np.linspace(-2,2,20)
t = np.linspace(-2,2,20)
S,T = np.meshgrid(s,t)
X = S-T
Y = S+T
Z = S+T
ax.plot_surface(X,Y,Z,Color='g',EdgeColor='none',alpha=0.1)
for i in(w1,w2):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0],
               LineWidth=2,
               Color='b',
               mutation_scale=20,
               arrowstyle="-|>")
ax.arrow3D(0,0,0,
           0,-1,1,
           LineWidth=2,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
t = np.linspace(-2,2,20)
x = np.zeros_like(t)
y = -t
z = t.copy()
ax.plot(x,y,z,Color='k')
ax.plot(0,0,0,'ro',Color='r')
plt.grid('on')
plt.show()

















