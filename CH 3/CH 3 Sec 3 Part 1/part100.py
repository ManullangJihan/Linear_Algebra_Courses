#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:36:03 2020

@author: hanjiya
"""

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

plt.rcParams['figure.figsize'] = [24,16]
plt.rcParams.update({'font.size' : 18})

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.arrow3D(0,0,0,2,1,0,LineWidth=3,Color='b',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,3,1,LineWidth=3,Color='b',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,3,LineWidth=3,Color='b',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,2,-5,4,LineWidth=3,Color='m',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,2,1,0,LineWidth=1,Color='r',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,-6,2,LineWidth=3,Color='b',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,6,LineWidth=3,Color='b',mutation_scale=20,arrowstyle="-|>")

ax.plot([2,2,0],[1,-5,-6],[0,-2,-2],'--',Color='r')
ax.plot([2,2,0,0,2],[1,-5,-6,0,1],[6,4,4,6,6],'--',Color='r')
ax.plot([2,2],[1,1],[0,6],'--',Color='r')
ax.plot([2,2],[-5,-5],[-2,4],'--',Color='r')
ax.plot([0,0],[-6,-6],[-2,4],'--',Color='r')
ax.plot([0,0],[0,0],[0,3],'--',Color='r')

ax.text(0.2,3,1,'(0,3,1)',Color='b')
ax.text(0,0.3,3,'(0,0,3)',Color='b')
ax.text(2,1.3,0,'1(2,1,0)',Color='r')
ax.text(2,1.5,.5,'(2,1,0)',Color='b')
ax.text(0,-6.5,-1.2,'-2(0,3,1)',Color='r')
ax.text(0,0,6.3,'2(0,0,3)',Color='r')
ax.text(2.2,-5.2,4.5,'(2,-5,4)',Color='m')

ax.set_xlim3d(-1,4)
ax.set_ylim3d(-7,4)
ax.set_zlim3d(-3,7)

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

plt.grid('on')

plt.show()