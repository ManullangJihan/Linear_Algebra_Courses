#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:49:56 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
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
v1 = np.array([[2,2,0]]).T
v2 = np.array([[-1,2,0]]).T
v3 = np.array([[0,0,1]]).T
b = np.array([[3,6,2]]).T

A = np.array([[2,-1,0,3],[2,2,0,6],[0,0,1,2]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([[r1,r2-r1,r3]]).T
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([0.5*r1,1/3*r2,r3])

C = 2*v1 + v2 + 2*v3
print(C)

# Visualize Our Answer
from mpl_toolkits.mplot3d.axes3d import Axes3D
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

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.arrow3D(0,0,0,2,2,0,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,-1,2,0,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,1,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,3,6,2,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,4,4,0,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,-1,2,0,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,2,Color='b',LineWidth=2,mutation_scale=20,arrowstyle="-|>")

ax.plot([4,3,-1],[4,6,2],[0,0,0],'--',)
ax.plot([4,3,-1,0,4],[4,6,2,0,4],[2,2,2,2,2],'--',)
ax.plot([4,4],[4,4],[0,2],'--',)
ax.plot([3,3],[6,6],[0,2],'--',)
ax.plot([-1,-1],[2,2],[0,2],'--',)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(-2,6)
plt.ylim(-1,7)

plt.show()
