#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:17:05 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import Matrix
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

v1 = np.array([[2,1,1]]).T
v2 = np.array([[-1,0,2]]).T
v3 = np.array([[2,-5,1]]).T
x = np.array([[4,-3,7]]).T
print(np.dot(v1.T,v2))
print(np.dot(v1.T,v3))
print(np.dot(v2.T,v3))
print(np.dot(x.T,v1))
print(np.dot(x.T,v2))
print(np.dot(x.T,v3))
print(np.dot(v1.T,v1))
print(np.dot(v2.T,v2))
print(np.dot(v3.T,v3))
c1 = np.dot(x.T,v1) / np.dot(v1.T,v1)
c2 = np.dot(x.T,v2) / np.dot(v2.T,v2)
c3 = np.dot(x.T,v3) / np.dot(v3.T,v3)
print(c1)
print(c2)
print(c3)
print(x == c1*v1+c2*v2+c3*v3)

w1 = 2*v1
w2 = 2*v2
w3 = v3.copy()
w = w1 + w2 + w3
ax.arrow3D(0,0,0,
           v1[0,0],v1[1,0],v1[2,0],
           LineWidth=6,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='b')
ax.arrow3D(0,0,0,
           v2[0,0],v2[1,0],v2[2,0],
           LineWidth=6,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='b')
ax.arrow3D(0,0,0,
           v3[0,0],v3[1,0],v3[2,0],
           LineWidth=6,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='b')
ax.arrow3D(0,0,0,
           w1[0,0],w1[1,0],w1[2,0],
           LineWidth=2,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='r')
ax.arrow3D(0,0,0,
           w2[0,0],w2[1,0],w2[2,0],
           LineWidth=2,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='r')
ax.arrow3D(0,0,0,
           w3[0,0],w3[1,0],w3[2,0],
           LineWidth=2,
           mutation_scale=20,
           arrowstyle="-|>",
           Color='r')
ax.plot([4,6,2],[2,-3,-5],[2,3,1],'--')

ax.plot([w2[0,0],w1[0,0]+w2[0,0],w[0,0],w2[0,0]+w3[0,0],w2[0,0]],
        [w2[1,0],w1[1,0]+w2[1,0],w[1,0],w2[1,0]+w3[1,0],w2[1,0]],
        [w2[2,0],w1[2,0]+w2[2,0],w[2,0],w2[2,0]+w3[2,0],w2[2,0]], '--')


ax.plot([w1[0,0]+w2[0,0],w1[0,0],w1[0,0]+w3[0,0]],
        [w1[1,0]+w2[1,0],w1[1,0],w1[1,0]+w3[1,0]],
        [w1[2,0]+w2[2,0],w1[2,0],w1[2,0]+w3[2,0]],'--')


ax.plot([w3[0,0],w1[0,0]+w3[0,0],w[0,0],w2[0,0]+w3[0,0],w3[0,0]],
        [w3[1,0],w1[1,0]+w3[1,0],w[1,0],w2[1,0]+w3[1,0],w3[1,0]],
        [w3[2,0],w1[2,0]+w3[2,0],w[2,0],w2[2,0]+w3[2,0],w3[2,0]],'--')

ax.text(4.4,2.2,2.2,'2u_1')
ax.text(-2.2,0,4.4,'2u_2')
ax.text(2.2,-5.5,1.1,'u_3')
ax.text(4.4,-3.3,7.7,'2u_1+2u_2+u_3')

plt.show()

v1 = Matrix([[2,1,1]]).T
v2 = Matrix([[-1,0,2]]).T
v3 = Matrix([[2,-5,1]]).T
x = Matrix([[4,-3,7]]).T
A = v1.col_insert(1,v2).col_insert(2,v3).col_insert(3,x)
c1_c2_c3 = A.rref()
print(c1_c2_c3)
