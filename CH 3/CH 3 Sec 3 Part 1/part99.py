#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:26:20 2020

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


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.arrow3D(0,0,0,1,0,0,LineWidth=2,Color='b',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,1,0,LineWidth=2,Color='b',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,1,LineWidth=2,Color='b',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,2,3,3,LineWidth=2,Color='b',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,2,0,0,LineWidth=1,Color='r',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,3,0,LineWidth=1,Color='r',mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,3,LineWidth=1,Color='r',mutation_scale=20,arrowstyle="-|>")

ax.plot([2,2,0],[0,3,3],[0,0,0],'--',Color='r')
ax.plot([2,2,0,0,2],[0,3,3,0,0],[3,3,3,3,3],'--',Color='r')
ax.plot([2,2],[0,0],[0,3],'--',Color='r')
ax.plot([2,2],[3,3],[0,3],'--',Color='r')
ax.plot([0,0],[3,3],[0,3],'--',Color='r')
ax.plot([0,0],[0,0],[0,3],'--',Color='r')

ax.text(1,0,0.2,'e_1')
ax.text(0,1,0.2,'e_2')
ax.text(0,0,1.2,'e_3')
ax.text(2.2,0,0.2,'2e_1')
ax.text(0,3,0.2,'3e_2')
ax.text(0,0,3.2,'3e_3')
ax.text(2.2,3.2,3.2,'(2,3,3)')


ax.set_xlim3d(-1,4)
ax.set_ylim3d(-1,4)
ax.set_zlim3d(-1,4)
plt.grid('on')
plt.show()