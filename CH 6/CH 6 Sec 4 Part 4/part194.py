#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:28:48 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

##
plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

## 1
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S +T
Y = 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.plot([0,0],[0,0],[-0.5,3],
        LineWidth=1,Color='k')
ax.arrow3D(0,0,0,2,0,0,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,1,2,0,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,3,2,2,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,1,
           LineWidth=2,Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.text(2.2,0,0,'v_1')
ax.text(1.1,2.2,0,'v_2')
ax.text(3.2,2.2,2.20,'v')
ax.text(0,0,1.1,'x')
ax.text(2,2,0,'col(A)')
ax.text(0,0,2.5,'col(A) = N(A^T)',
        BackgroundColor='w')
ax.set_xlim(-0.5,3)
ax.set_ylim(-0.5,3)
ax.set_zlim(-0.5,3)

plt.grid('on')
plt.show()

## 2
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S+T
Y = 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.plot([0,0],[0,0],[-0.5,3],
        LineWidth=1,Color='k')
ax.arrow3D(0,0,0,2,0,0,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,1,2,0,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,3,2,2,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,1,
           LineWidth=2,Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,2,
           LineWidth=2,Color='g',
           mutation_scale=20,
           arrowstyle="-|>")
ax.plot([0,3],[0,2],[2,2],'--',LineWidth=2, Color='k')

ax.text(2.2,0,0,'v_1')
ax.text(1.1,2.2,0,'v_2')
ax.text(3.2,2.2,2.20,'v')
ax.text(0,0,1.1,'x')
ax.text(2,2,0,'col(A)')
ax.text(0,0,2.5,'col(A) = N(A^T)',
        BackgroundColor='w')
ax.set_xlim(-0.5,3)
ax.set_ylim(-0.5,3)
ax.set_zlim(-0.5,3)
plt.grid('on')
plt.show()


## 3
fig = plt.figure()
ax = fig.gca(projection='3d')
s = np.linspace(-4,4,20)
t = np.linspace(-4,4,20)
S,T = np.meshgrid(s,t)
X = 2*S+T
Y = 2*T
Z = np.zeros_like(T)
ax.plot_surface(X,Y,Z,EdgeColor='none',LineWidth=0,alpha=0.2)
ax.plot([0,0],[0,0],[-0.5,3],
        LineWidth=1,Color='k')
ax.arrow3D(0,0,0,2,0,0,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,1,2,0,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,3,2,2,
           LineWidth=2,Color='b',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,1,
           LineWidth=2,Color='r',
           mutation_scale=20,
           arrowstyle="-|>")
ax.arrow3D(0,0,0,0,0,2,
           LineWidth=2,Color='g',
           mutation_scale=20,
           arrowstyle="-|>")
ax.plot([0,3],[0,2],[2,2],'--',LineWidth=2, Color='k')

ax.text(2.2,0,0,'v_1')
ax.text(1.1,2.2,0,'v_2')
ax.text(3.2,2.2,2.20,'v')
ax.text(0,0,1.1,'x')
ax.text(2,2,0,'col(A)')
ax.text(0,0,2.5,'col(A) = N(A^T)',
        BackgroundColor='w')
ax.set_xlim(-0.5,3)
ax.set_ylim(-0.5,3)
ax.set_zlim(-0.5,3)
plt.grid('on')
plt.show()