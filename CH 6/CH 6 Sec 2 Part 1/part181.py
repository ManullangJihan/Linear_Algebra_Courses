#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:07:18 2020

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

fig = plt.figure()
ax = fig.gca(projection='3d')

u = np.array([[1,-1,1]]).T
x = np.linspace(-3,3,20)
y = np.linspace(-3,3,20)
X,Y = np.meshgrid(x,y)
Z = -X+Y
ax.plot_surface(X,Y,Z,EdgeColor='g',alpha=0.05)
ax.arrow3D(0,0,0,
           u[0,0],u[1,0],u[2,0],
           LineWidth=2,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='r')
ax.text(1,-1,1,'u')
plt.show()

## 
fig = plt.figure()
ax = fig.gca(projection='3d')

u = np.array([[1,-1,1]]).T
v = np.array([[0,1,1]]).T
w = np.array([[-2,-1,1]]).T
x = np.linspace(-3/2,3/2,20)
y = np.linspace(-3/2,3/2,20)
S,T = np.meshgrid(x,y)
X = -2*T
Y = S-T
Z = S+T
ax.plot_surface(X,Y,Z,alpha=0.1)
ax.arrow3D(0,0,0,
           u[0,0],u[1,0],u[2,0],
           LineWidth=2,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='r')
ax.arrow3D(0,0,0,
           v[0,0],v[1,0],v[2,0],
           LineWidth=2,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='b')
ax.arrow3D(0,0,0,
           w[0,0],w[1,0],w[2,0],
           LineWidth=2,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='b')
ax.text(1,-1,1,' u')
ax.text(0,1.5,1.5,'v')
ax.text(-3,-1.5,1.5,' w')
plt.show()