#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:08:13 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

s = np.linspace(-1.5,1.5,15)
t = np.linspace(-1.5,1.5,15)
S,T = np.meshgrid(s,t)
X = S
Y = T
Z = S-T
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,Color='g',alpha=0.5)
ax.plot(0,0,0,'o',Color='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#
s = np.linspace(-1.5,1.5,15)
t = np.linspace(-1.5,1.5,15)
S,T = np.meshgrid(s,t)
X = S
Y = T
Z = S-T
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,Color='r',alpha=0.5)
ax.plot_surface(X,Y,Z+2,Color='r',alpha=0.5)
ax.plot(0,0,0,'o',Color='r')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#
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

s = np.linspace(-1.5,1.5,15)
t = np.linspace(-1.5,1.5,15)
S,T = np.meshgrid(s,t)
X = S
Y = T
Z = S-T
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,Color='k',alpha=0.5)
ax.arrow3D(0,0,0,-1,0,3,Color='b',LineWidth=1,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,1,0,1,Color='b',LineWidth=1,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,4,Color='r',LineWidth=1,mutation_scale=20,arrowstyle="-|>")
ax.plot(0,0,0,'o',Color='m')
ax.plot(1,0,1,'o',Color='m' )
ax.plot(0,0,4,'o',Color='m' )
ax.plot(-1,0,3,'o',Color='m' )
ax.plot([1,0,-1],[0,0,0],[1,4,3],'--',Color='b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')