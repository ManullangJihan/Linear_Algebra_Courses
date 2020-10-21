#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:14:17 2020

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
v2 = np.array([[0,2,0]]).T
v = np.array([[1,1,1]]).T
w1 = v1.copy()
w2 = v2.copy()
pw1v = (np.dot(v.T,w1) / np.dot(w1.T,w1) @ w1.T).T
pw2v = (np.dot(v.T,w2) / np.dot(w2.T,w2) @ w2.T).T
p = pw1v + pw2v

fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S
Y = 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',Color='m',alpha=0.1)
ax.arrow3D(0,0,0,
           2,0,0,
           LineWidth=1,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           0,2,0,
           LineWidth=1,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           1,1,1,
           LineWidth=1,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           1,0,0,
           LineWidth=2,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           0,1,0,
           LineWidth=2,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           1,1,0,
           LineWidth=2,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           0,0,1,
           LineWidth=2,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(1,1,0,
           0,0,1,
           LineWidth=2,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.plot([1,1,0],[0,1,1],[0,1,0],'--',Color='k')
ax.plot([1,1,0],[0,1,1],[0,0,0],'--',Color='k')
ax.plot([1,1],[1,1],[0,1],'--',Color='k')
ax.text(2.1,0,0,'w_1')
ax.text(0,2.3,0,'w_2')
ax.text(1.1,1.1,1.1,'v')
ax.text(0.8,-0.3,0,'proj_{w_1}v')
ax.text(-0.7,1,0,'proj_{w_2}v')
ax.text(1.1,1.1,0,'w')
ax.text(0,0,1.1,'u')

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-1,2)

plt.xlabel('x-axis')
plt.grid('on')
plt.show()



