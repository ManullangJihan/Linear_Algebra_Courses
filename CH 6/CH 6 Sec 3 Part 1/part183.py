#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:03:29 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

y = np.array([[-3,3]]).T
u = np.array([[-5,1]]).T
proj = (np.dot(y.T,u) / np.dot(u.T,u) @ u.T).T

fig = plt.figure(0)
ax = fig.gca()
ax.arrow(0,0,y[0,0],y[1,0],LineWidth=1,Color='b')
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=1,Color='b')

ax.set_xlim(-6,0)
ax.set_ylim(0,6)

plt.xticks(np.arange(-6,0))
plt.yticks(np.arange(0,6))
ax.text(-3,3.3,'y=(-3,3)')
ax.text(-5,1.3,'u=(-5,1)')
plt.grid('on')
plt.show()

fig = plt.figure(0)
ax = fig.gca()
ax.arrow(0,0,y[0,0],y[1,0],LineWidth=2,Color='b')
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=2,Color='b')
ax.arrow(0,0,proj[0,0],proj[1,0],LineWidth=2, Color='r')
ax.plot([proj[0,0],y[0,0]],[proj[1,0],y[1,0]],LineWidth=2,Color='r')
ax.set_xlim(-6,0)
ax.set_ylim(0,6)

plt.xticks(np.arange(-6,0))
plt.yticks(np.arange(0,6))
ax.text(-3,3.3,'y=(-3,3)')
ax.text(-5,1.3,'u=(-5,1)')
ax.text(-2,0.8,'proj_u y')
plt.grid('on')
plt.show()

