#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:03:29 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.patches import FancyArrowPatch

v1 = np.array([[2,0,-1]]).T
v2 = np.array([[0,3,-1]]).T
v3 = np.array([[2,3,-2]]).T
v = np.array([[1,1,2]]).T
A = np.array([[2,0,2,1],[0,3,3,1],[-1,-1,-2,1]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([0.5*r1,r2,r3])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3+r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2,r3+1/3*r2])
print(A)

# Visualize Our Answer
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

s = np.linspace(-1.5,1.5,20)
t = np.linspace(-1.5,1.5,20)
S,T = np.meshgrid(s,t)
X = 2*S
Y = 3*T
Z = -S - T
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,Color='g')
ax.arrow3D(0,0,0,2,0,-1,Color='b',LineWidth=2,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,3,-1,Color='b',LineWidth=2,arrowstyle="-|>")
ax.arrow3D(0,0,0,2,3,-2,Color='b',LineWidth=2,arrowstyle="-|>")
ax.arrow3D(0,0,0,1,1,2,Color='b',LineWidth=2,arrowstyle="-|>")
ax.plot([2,2,0],[0,3,3],[-1,-2,-1],'--',LineWidth=1)
ax.text(2.4,0,-1,'v_1')
ax.text(0,3.3,-1,'v_2')
ax.text(2,2,-2,'v_3')
ax.text(1,1,2.3,'v')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
