#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:24:31 2020

@author: hanjiya
"""

import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
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


a,b,c,d = symbols('a,b,c,d')
A = Matrix([[1,2,3,a],[1,1,2,b],[2,1,3,c]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = Matrix([r1,r2-r1,r3-2*r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = Matrix([r1,-0.5*r2,r3])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = Matrix([r1,r2,r3+3*r2])
print(A)

# Cara Cepat
A = Matrix([[1,2,3,a],[1,1,2,b],[2,1,3,c]])
A_Matrix, A_piv = A.rref()
print(A_Matrix)

# Visualisasi
s = np.linspace(-2,2,20)
t = np.linspace(-2,2,20)
S,T = np.meshgrid(s,t)
fig = plt.figure()
a = 3*S-T
b = S
c = T
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(a,b,c,Color='k')
ax.arrow3D(0,0,0,3,1,0,Color='white', LineWidth=4, mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,-1,0,1,Color='white', LineWidth=4, mutation_scale=20,arrowstyle="-|>")

plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('a-axis')
plt.ylabel('b-axis')




