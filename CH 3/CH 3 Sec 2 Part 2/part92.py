#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:24:04 2020

@author: hanjiya
"""

import numpy as np
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

#
s = np.linspace(-1.5,1.5,20)
t = np.linspace(-1.5,1.5,20)
S,T = np.meshgrid(s,t)
X = S-T
Y = S+T
Z = 2*S+2*T
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,Color='r',alpha=0.2)
ax.plot(0,0,0,'o',Color='r')
u = np.array([[1,1,2]]).T
v = np.array([[-1,1,2]]).T
x = np.array([[1,-1]]).T
A = np.array([u,v]).T
AtimesX = A @ x
V = 2 * np.random.rand(2,6) -1
vecs = A @ V
print(vecs)
plt.show()


#
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-1.5,1.5,20)
t = np.linspace(-1.5,1.5,20)
S,T = np.meshgrid(s,t)
X = S-T
Y = S+T
Z = 2*S+2*T
ax.plot_surface(X,Y,Z,Color='g',alpha=0.1)
ax.plot(0,0,0,'o',Color='r')
u = np.array([[1,1,2]]).T
v = np.array([[-1,1,2]]).T
x = np.array([[1,-1]]).T
A = np.array([u,v]).T
AtimesX = A @ x
V = 2 * np.random.rand(2,6) - 1
Vecs = A @ V
Vecs = np.reshape(Vecs,(3,6))
for k in range(0,6):
    ax.arrow3D(0,0,0,Vecs[0,k],Vecs[1,k],Vecs[2,k],LineWidth=1,arrowstyle="-|>")

plt.show()


# 
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-1.5,1.5,20)
t = np.linspace(-1.5,1.5,20)
S,T = np.meshgrid(s,t)
X = S-T
Y = S+T
Z = 2*S+2*T
ax.plot_surface(X,Y,Z,Color='g',alpha=0.1)
ax.plot(0,0,0,'o',Color='r')
u = np.array([[1,1,2]]).T
v = np.array([[-1,1,2]]).T
x = np.array([[1,-1]]).T
A = np.array([u,v]).T
AtimesX = A @ x
V = 2 * np.random.rand(2,100) - 1
Vecs = A @ V
Vecs = np.reshape(Vecs,(3,100))
for k in range(0,100):
    ax.arrow3D(0,0,0,Vecs[0,k],Vecs[1,k],Vecs[2,k],LineWidth=1,arrowstyle="-|>")

plt.show()
    
