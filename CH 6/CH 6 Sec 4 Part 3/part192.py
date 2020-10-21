#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:45:01 2020

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

v1 = np.array([[2,0,0]]).T
v2 = np.array([[1,2,0]]).T
v = np.array([[3,2,2]]).T
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S + T
Y = 2*T
Z = np.zeros_like(T)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X,Y,Z,EdgeColor='none',Color='g',LineWidth=0,alpha=0.2)
for i in(v1,v2,v):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0],
               LineWidth=2,
               Color='b',
               mutation_scale=20,
               arrowstyle="-|>")
ax.text(2.1,0,0,'v_1')
ax.text(1.1,2.2,0,'v_2')
ax.text(3.3,2.2,2.2,'v')
ax.set_xlim(-0.5,4)
ax.set_ylim(-0.5,4)
ax.set_zlim(-0.5,4)

plt.grid('on')
plt.show()

## 2
v1 = np.array([[2,0,0]]).T
v2 = np.array([[1,2,0]]).T
v = np.array([[3,2,2]]).T
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S + T
Y = 2*T
Z = np.zeros_like(T)
projv1v = (np.dot(v.T,v1)/np.dot(v1.T,v1) @ v1.T).T
projv2v = (np.dot(v.T,v2)/np.dot(v2.T,v2) @ v2.T).T

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X,Y,Z,EdgeColor='none',Color='g',LineWidth=0,alpha=0.2)
for i in(v1,v2,v):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0],
               LineWidth=2,
               Color='b',
               mutation_scale=20,
               arrowstyle="-|>")
for i in(projv1v,projv2v):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0],
               LineWidth=1,
               Color='r',
               mutation_scale=20,
               arrowstyle="-|>")
    
ax.text(2.1,0,0,'v_1')
ax.text(1.1,2.2,0,'v_2')
ax.text(3.3,2.2,2.2,'v')
ax.text(3.3,0,0,'p_1')
ax.text(1.54,3.08,0,'p_2')
ax.set_xlim(-0.5,4)
ax.set_ylim(-0.5,4)
ax.set_zlim(-0.5,4)

plt.grid('on')
plt.show()

## 3
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S + T
Y = 2*T
Z = np.zeros_like(T)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X,Y,Z,EdgeColor='none',Color='g',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,
           2,0,0,
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           1,2,0,
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           3,2,2,
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           3,0,0,
           LineWidth=1,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           7/5,14/5,0,
           LineWidth=1,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           22/5,14/5,0,
           LineWidth=1,Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           -7/5,-4/5,2,
           LineWidth=1,Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(22/5,14/5,0,
           -7/5,-4/5,2,
           LineWidth=1,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.plot([3,3,7/5],[0,2,14/5],[0,2,0],'--',LineWidth=1,Color='k')
ax.plot([3,22/5,7/5],[0,14/5,14/5],[0,0,0],'--',LineWidth=1,Color='k')

ax.text(2.1,0,0,'v_1')
ax.text(1.1,2.2,0,'v_2')
ax.text(3.3,2.2,2.2,'v')
ax.text(3.3,0,0,'p_1')
ax.text(1.54,3.08,0,'p_2')
ax.text(-1.54,-0.88,2.2,'u')

ax.set_xlim(-1.5,5)
ax.set_ylim(-1.5,4)
ax.set_zlim(-0.5,4)

plt.grid('on')
plt.show()