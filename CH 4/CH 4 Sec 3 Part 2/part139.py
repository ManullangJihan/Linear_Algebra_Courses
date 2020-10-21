#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:02:59 2020

@author: hanjiya
"""

from sympy import symbols, Matrix
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

plt.rcParams['figure.figsize'] = [16,8]
plt.rcParams.update({'font.size':10})

x,y,z = symbols('x,y,z')
A = Matrix([[1,-1,2]])
s = Matrix([[x,y,z]]).T
T = A @ s
T1 = T.subs([(x,1),(y,0),(z,0)])
T2 = T.subs([(x,0),(y,1),(z,0)])
T3 = T.subs([(x,0),(y,0),(z,1)])

print(T1)
print(T2)
print(T3)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.arrow3D(0,0,0,
           1,1,0,
           mutation_scale=20,
           ec ='green',
           fc='red')
ax.arrow3D(0,0,0,
           -1,0,1,
           mutation_scale=20,
           ec ='green',
           fc='red')
ax.arrow3D(0,0,0,
           2,2,1,
           mutation_scale=20,
           ec ='green',
           fc='red')

s = np.linspace(0,1,20)
t = np.linspace(0,1,20)
S,T = np.meshgrid(s,t)
X = S+2*T
Y = S+2*T
Z = T
ax.plot_surface(X,Y,Z,EdgeColor='g',alpha=0.1)

ax.set_xlim(-1,3)
ax.set_ylim(-1,3)
ax.set_zlim(0,1)
plt.grid('on')
plt.show()
