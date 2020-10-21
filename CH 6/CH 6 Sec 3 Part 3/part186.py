#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:15:26 2020

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

v1 = np.array([[1,1,0]]).T
v2 = np.array([[0,1,0]]).T
v3 = np.array([[0,1,1]]).T
s = np.linspace(-3,3,20)
t = np.linspace(-3,3,20)
S,T = np.meshgrid(s,t)
X = S
Y = S+T
Z = np.zeros((20,20))

ax.plot_surface(X,Y,Z,EdgeColor='none',Color='g',alpha=0.1)
for i in(v1,v2):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0],
               LineWidth=2,
               Color='b',
               mutation_scale=20,
               arrowstyle="-|>")

ax.text(1.1,1.1,0,'v_1')
ax.text(0,1.2,0,'v_2')
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-0.2,1.2)
ax.set_zlim(0,1)
plt.show()

## 2
fig = plt.figure()
ax = fig.gca(projection='3d')

v1 = np.array([[1,1,0]]).T
v2 = np.array([[0,1,0]]).T
v3 = np.array([[0,1,1]]).T
w1 = v1.copy()
proj = (np.dot(v2.T,w1) / np.dot(w1.T,w1) @ w1.T).T
w2 = v2 - proj
s = np.linspace(-3,3,20)
t = np.linspace(-3,3,20)
S,T = np.meshgrid(s,t)
X = S
Y = S+T
Z = np.zeros((20,20))
ax.plot_surface(X,Y,Z,EdgeColor='none',FaceColor='g',alpha=0.1)
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
ax.plot([proj[0,0],v2[0,0],w2[0,0]],
        [proj[1,0],v2[1,0],w2[1,0]],
        [proj[2,0],v2[2,0],w2[2,0]],
        '--',Color='r')

ax.text(1.1,1.1,0,'v_1')
ax.text(0,1.2,0,'v_2')
ax.text(-0.6,0.6,0,'w_2')
ax.text(1,0.9,0,'w_1')
ax.text(0.45,0.3,0,'proj_{w_1} v_2')
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-0.2,1.2)
ax.set_zlim(0,1)
plt.show()

## 3
fig = plt.figure()
ax = fig.gca(projection='3d')

v1 = np.array([[1,1,0]]).T
v2 = np.array([[0,1,0]]).T
v3 = np.array([[0,1,1]]).T
w1 = v1.copy()
proj = (np.dot(v2.T,w1) / np.dot(w1.T,w1) @ w1.T).T
w2 = v2 - proj
w2 = 2*w2
s = np.linspace(-3,3,20)
t = np.linspace(-3,3,20)
S,T = np.meshgrid(s,t)
X = S
Y = S+T
Z = np.zeros((20,20))
ax.plot_surface(X,Y,Z,EdgeColor='none',FaceColor='g',alpha=0.1)
for i in(w1,w2):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0],
               LineWidth=2,
               Color='b',
               mutation_scale=20,
               arrowstyle="-|>")
ax.arrow3D(0,0,0,
           v3[0,0],v3[1,0],v3[2,0],
           LineWidth=2,
           Color='r',
           mutation_scale=20,
           arrowstyle="-|>")

ax.text(1.1,1.1,0,'v_1')
ax.text(0,1.2,0,'v_2')
ax.text(-0.6,0.6,0,'w_2')
ax.text(1,0.9,0,'w_1')
ax.text(0.45,0.3,0,'proj_{w_1} v_2')
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-0.2,1.2)
ax.set_zlim(0,1)
plt.show()


##
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-3,3,20)
t = np.linspace(-3,3,20)
S,T = np.meshgrid(s,t)
X = S
Y = S+T
Z = np.zeros((20,20))
pw1v2 = (np.dot(v2.T,w1)/np.dot(w1.T,w1) @ w1.T).T
pw1v3 = (np.dot(v3.T,w1)/np.dot(w1.T,w1) @ w1.T).T
pw2v3 = (np.dot(v3.T,w2)/np.dot(w2.T,w2) @ w2.T).T
w = pw1v3+pw2v3
w3 = v3-w
ax.plot_surface(X,Y,Z,EdgeColor='none',FaceColor='g',alpha=0.1)
for i in(w1,w2,w3):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0],
               LineWidth=2,
               Color='r',
               mutation_scale=20,
               arrowstyle="-|>")
    
for i in(pw1v3,pw2v3,w):
    ax.arrow3D(0,0,0,
               i[0,0],i[1,0],i[2,0],
               LineWidth=2,
               Color='k',
               mutation_scale=20,
               arrowstyle="-|>")
ax.arrow3D(0,0,0,
           v3[0,0],v3[1,0],v3[2,0],
           LineWidth=2,
           Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.plot([pw1v3[0,0],v3[0,0],pw2v3[0,0]],
        [pw1v3[1,0],v3[1,0],pw2v3[1,0]],
        [pw1v3[2,0],v3[2,0],pw2v3[2,0]],
        '--',Color='k')
ax.plot([pw1v3[0,0],w[0,0],pw2v3[0,0]],
        [pw1v3[1,0],w[1,0],pw2v3[1,0]],
        [pw1v3[2,0],w[2,0],pw2v3[2,0]],
        '--',Color='k')
ax.plot([w3[0,0],v3[0,0]],
        [w3[1,0],v3[1,0]],
        [w3[2,0],v3[2,0]],
        '--',Color='k')

ax.text(1,0.9,0,'w_1')
ax.text(-1.1,1.1,0,'w_2')
ax.text(0,1.1,1.1,'v_3')
ax.text(0.5,0.4,0,'proj_{w_1}v_3')
ax.text(-0.8,0.4,0,'proj_{w_2}v_3')
ax.text(0,1.15,0,'w')
ax.text(0,1.5,0.5,'v_3-w')
ax.text(0,0,1.1,'w_3')

ax.set_xlim(-1.2,1.2)
ax.set_ylim(-0.2,1.2)
ax.set_zlim(0,1)
plt.show()

