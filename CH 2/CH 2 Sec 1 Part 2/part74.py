#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:43:00 2020

@author: hanjiya
"""

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

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.arrow3D(0,0,0,1,0,0,Color='b', LineWidth=2, mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,1,0,Color='b', LineWidth=2, mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,1,Color='b', LineWidth=2, mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,2,0,0,Color='m', LineWidth=1, mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,3,0,Color='m', LineWidth=1, mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,5,Color='m', LineWidth=1, mutation_scale=20,arrowstyle="-|>")
ax.arrow3D(0,0,0,2,3,5,Color='b', LineWidth=2, mutation_scale=20,arrowstyle="-|>")

ax.plot([2,2],[3,0],[0,0],'--',Color='b')
ax.plot([0,2],[3,3],[0,0],'--',Color='b')
ax.plot([2,0],[3,3],[5,5],'--',Color='b')
ax.plot([2,2],[3,3],[5,0],'--',Color='b')
ax.plot([0,0],[3,3],[0,5],'--',Color='b')
ax.plot([2,2],[0,0],[0,5],'--',Color='b')
ax.plot([2,2],[0,3],[5,5],'--',Color='b')
ax.plot([0,0],[0,3],[5,5],'--',Color='b')
ax.plot([2,0],[0,0],[5,5],'--',Color='b')
ax.plot([2,2],[3,3],[0,0],'--',Color='b')

ax.text(2.7,0,0,'2e_1')
ax.text(0,3.2,0,'3e_2')
ax.text(0,0,5.3,'5e_3')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(-1,3)
plt.ylim(-1,4)

plt.show()














