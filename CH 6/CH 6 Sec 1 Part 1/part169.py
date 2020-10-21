#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:14:58 2020

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


plt.rcParams['figure.figsize'] = [20,18]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca(projection='3d')

u = np.linspace(-np.pi, np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
u1 = np.array([[3,0,4]]).T

ax.plot_surface(5*x,5*y,5*z, EdgeColor='g',alpha=0.1)
ax.plot([-7,7],[0,0],[0,0],LineWidth=1,Color='k')
ax.plot([0,0],[-7,7],[0,0],LineWidth=1,Color='k')
ax.plot([0,0],[0,0],[-7,7],LineWidth=1,Color='k')
ax.arrow3D(0,0,0,u[0],u[1],u[2], mutation_scale=20, arrowstyle="->", color="b",LineWidth=10)
plt.show()
