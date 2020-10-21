#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:12:07 2020

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

##
plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

## 1
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S
Y = 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,2,0,0,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,2,0,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,3,2,2,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.text(2.2,0,0,'w_1')
ax.text(0,2.2,0,'w_2')
ax.text(3.3,2.2,2.2,'v')

ax.set_xlim(-0.5,4)
ax.set_ylim(-0.5,4)
ax.set_zlim(-0.5,4)

plt.grid('on')
plt.show()

## 2
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S
Y = 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,2,0,0,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,2,0,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,3,2,2,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,3,0,0,
           LineWidth=0.5,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,2,0,LineWidth=0.5,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.plot([3,3,0],[0,2,2],[0,2,0],
        '--',LineWidth=1,Color='k')
ax.text(2.2,0,0,'w_1')
ax.text(0,2.2,0,'w_2')
ax.text(3.3,2.2,2.2,'v')
ax.text(3.4,0,0,'p_1')
ax.text(0,2.2,0,'p_2')

ax.set_xlim(-0.5,4)
ax.set_ylim(-0.5,4)
ax.set_zlim(-0.5,4)

plt.grid('on')
plt.show()


## 3
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S
Y = 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,2,0,0,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,2,0,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,3,2,2,LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,3,0,0,
           LineWidth=0.5,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,2,0,LineWidth=0.5,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,2,LineWidth=0.5,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.plot([3,3,0],[0,2,2],[0,2,0],
        '--',LineWidth=1,Color='k')
ax.plot([3,3,0],[0,2,2],[0,0,0],
        '--',LineWidth=1,Color='k')
ax.text(2.2,0,0,'w_1')
ax.text(0,2.2,0,'w_2')
ax.text(3.3,2.2,2.2,'v')
ax.text(3.4,0,0,'p_1')
ax.text(0,2.2,0,'p_2')
ax.text(0,0,2.2,'u')
ax.text(3.3,2.2,0,'w')

ax.set_xlim(-0.5,4)
ax.set_ylim(-0.5,4)
ax.set_zlim(-0.5,4)

plt.xlabel('x')
plt.ylabel('y')

plt.grid('on')
plt.show()