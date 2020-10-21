#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:50:44 2020

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

v1 = np.array([[1,-3,0]]).T
v2 = np.array([[2,2,0]]).T
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = S + 2*T
Y = -3*S + 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='g',alpha=0.1)
ax.arrow3D(0,0,0,
           v1[0,0],v1[1,0],v1[2,0],
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,
           v2[0,0],v2[1,0],v2[2,0],
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-1,1)
ax.text(1.1,-3.3,0,'v_1')
ax.text(2.2,2.2,0,'v_2')

## 
fig = plt.figure()
ax = fig.gca(projection='3d')

v1 = np.array([[1,-3,0]]).T
v2 = np.array([[2,2,0]]).T
w1 = v1.copy()
proj = (np.dot(v2.T,v1) / np.dot(v1.T,v1) @ v1.T).T
w2 = v2 - proj
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = S + 2*T
Y = -3*S + 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='g',alpha=0.1)

for i in(v1,v2):
    ax.arrow3D(0,0,0,
           i[0,0],i[1,0],i[2,0],
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
for i in(w1,w2,proj):
    ax.arrow3D(0,0,0,
           i[0,0],i[1,0],i[2,0],
           LineWidth=2,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")

ax.plot(t,-3*t,np.zeros_like(t),'-',Color='k')
ax.plot([w2[0,0],v2[1,0],proj[2,0]],[w2[1,0],v2[1,0],proj[1,0]],[w2[2,0],v2[2,0],proj[2,0]],
        '--',Color='k');

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-1,1)
ax.text(1.1,-3.3,0,'v_1')
ax.text(2.2,2.2,0,'v_2')
ax.text(0.3,-3.3,0,'w_1')
ax.text(2.64,0.88,0,'w_2')
ax.text(-2,2,0,'proj_{w_1}v_2')

plt.xlabel('x-axis')
plt.show()
# =============================================================================
# ax.arrow3D(0,0,0,
#            v1[0,0],v1[1,0],v1[2,0],
#            LineWidth=2,
#            Color='b',
#            mutation_scale=20,
#            arrowstyle="-|>")
# ax.arrow3D(0,0,0,
#            v2[0,0],v2[1,0],v2[2,0],
#            LineWidth=2,
#            Color='b',
#            mutation_scale=20,
#            arrowstyle="-|>")
# =============================================================================
# =============================================================================
# ax.arrow3D(0,0,0,
#            w1[0,0],w1[1,0],w1[2,0],
#            LineWidth=2,
#            Color='r',
#            mutation_scale=20,
#            arrowstyle="-|>")
# ax.arrow3D(0,0,0,
#            w2[0,0],w2[1,0],w2[2,0],
#            LineWidth=2,
#            Color='r',
#            mutation_scale=20,
#            arrowstyle="-|>")
# ax.arrow3D(0,0,0,
#            proj[0,0],proj[1,0],proj[2,0],
#            LineWidth=2,
#            Color='r',
#            mutation_scale=20,
#            arrowstyle="-|>")
# =============================================================================