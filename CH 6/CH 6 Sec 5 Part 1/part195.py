#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:55:22 2020

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
s = np.linspace(-5,5,20)
t = np.linspace(-5,5,20)
S,T = np.meshgrid(s,t)
X = 2*S+T
Y = S+2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,2,1,0,
           LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,1,2,0,
           LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,4,4,2,
           LineWidth=1,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.text(2.2,1.1,0,'a_1',FontSize=12)
ax.text(1.1,2.2,0,'a_2',FontSize=12)
ax.text(4.1,4.1,2.1,'b',FontSize=12)
ax.text(1,4,0,'col(A)',FontSize=12)
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(-0.5,3)
plt.grid('on')
plt.show()

## 2
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-5,5,20)
t = np.linspace(-5,5,20)
S,T = np.meshgrid(s,t)
X = 2*S+T
Y = S+2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,2,1,0,
           LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,1,2,0,
           LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,4,4,2,
           LineWidth=1,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,4,4,0,
           LineWidth=1,Color='r')
ax.arrow3D(0,0,0,8/3,4/3,0,
           LineWidth=1,Color='r')
ax.arrow3D(0,0,0,4/3,8/3,0,
           LineWidth=1,Color='r')
ax.arrow3D(4,4,0,0,0,2,
           LineWidth=2,Color='k')
ax.plot([4,4],[4,4],[0,2],'--',Color='k')
ax.plot([4/3,4,8/3],[8/3,4,4/3],[0,0,0],'--',Color='k')

ax.text(2.2,1.1,0,'a_1',FontSize=12)
ax.text(1.1,2.2,0,'a_2',FontSize=12)
ax.text(4.1,4.1,2.1,'b',FontSize=12)
ax.text(1,4,0,'col(A)',FontSize=12)
ax.text(4.2,4.2,0,'w',FontSize=12)
ax.text(1,4,0,'col(A)',FontSize=12)
ax.text(4,3.8,1,'b-w',FontSize=12)

ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(-0.5,3)

plt.grid('on')
plt.show()


## 3
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-5,5,20)
t = np.linspace(-5,5,20)
S,T = np.meshgrid(s,t)
X = 2*S+T
Y = S+2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,2,1,0,
           LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,1,2,0,
           LineWidth=1,Color='b',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,4,4,2,
           LineWidth=1,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,4,4,0,
           LineWidth=1,Color='r')
ax.arrow3D(0,0,0,8/3,4/3,0,
           LineWidth=1,Color='r')
ax.arrow3D(0,0,0,4/3,8/3,0,
           LineWidth=1,Color='r')
ax.arrow3D(4,4,0,0,0,2,
           LineWidth=2,Color='k')
ax.plot([4,4],[4,4],[0,2],'--',Color='k')
ax.plot([4/3,4,8/3],[8/3,4,4/3],[0,0,0],'--',Color='k')

ax.text(2.2,1.1,0,'a_1',FontSize=12)
ax.text(1.1,2.2,0,'a_2',FontSize=12)
ax.text(4.1,4.1,2.1,'b',FontSize=12)
ax.text(1,4,0,'col(A)',FontSize=12)
ax.text(4.2,4.2,0,'w',FontSize=12)
ax.text(1,4,0,'col(A)',FontSize=12)
ax.text(4,3.8,1,'b-w',FontSize=12)

ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(-0.5,3)

plt.grid('on')
plt.show()

## 4
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-5,5,20)
t = np.linspace(-5,5,20)
S,T = np.meshgrid(s,t)
X = 3*S+T
Y = S+3*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,4,4,2,
           LineWidth=1,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,4,4,0,
           LineWidth=1,Color='r')
ax.arrow3D(4,4,0,0,0,2,
           LineWidth=2,Color='k')



ax.text(4.1,4.1,2.1,'b',FontSize=12)
ax.text(4.2,4.2,0,'w',FontSize=12)
ax.text(1,4,0,'col(A)',FontSize=12)
ax.text(4,3.8,1,'b-w',FontSize=12)

ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(-0.5,3)

plt.grid('on')
plt.show()

## 5
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-5,5,20)
t = np.linspace(-5,5,20)
S,T = np.meshgrid(s,t)
X = 3*S+T
Y = S+3*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.arrow3D(0,0,0,4,4,2,
           LineWidth=1,Color='r',
           mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,4,4,0,
           LineWidth=1,Color='r')
ax.arrow3D(4,4,0,0,0,2,
           LineWidth=2,Color='k')
ax.arrow3D(0,0,0,2,4,0,
           LineWidth=2,Color='k')
ax.arrow3D(2,4,0,2,0,0,
           LineWidth=2,Color='k')
ax.arrow3D(2,4,0,2,0,2,
           LineWidth=2,Color='k')


ax.text(2,2,1,'b',FontSize=12)
ax.text(2,2,0,'w',FontSize=12)
ax.text(4,1,0,'col(A)',FontSize=12)
ax.text(4,4.6,1,'b-w',FontSize=12)
ax.text(1,2,0,'u',FontSize=12,BackgroundColor='w')
ax.text(3,4.5,0,'w-u',FontSize=12)
ax.text(3,3.8,1,'b-u',FontSize=12)
ax.text(2,4.3,0,'A',FontSize=12)
ax.text(4,4.3,0,'B',FontSize=12)
ax.text(4,4,2.2,'C',FontSize=12)
ax.set_xlim(0,5)
ax.set_ylim(0,5)
ax.set_zlim(-0.5,3)

plt.grid('on')
plt.show()