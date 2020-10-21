#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:23:19 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca()

u = np.array([[4,1]]).T
v = np.array([[2,4]]).T
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=1,Color='b')
ax.arrow(0,0,v[0,0],v[1,0],LineWidth=1,Color='b')
ax.arrow(4,1,-2,3,LineWidth=1,Color='r')
t = np.linspace(np.arctan2(1,4),np.arctan2(4,2))
ax.plot(np.cos(t),np.sin(t),Color='k',LineWidth=1)

ax.set_xlim(-1,5)
ax.set_ylim(-1,5)
ax.text(2.1,4.1,'(2,4)')
ax.text(4,1,'(4,1)')
ax.text(0.9,0.7,'theta')
ax.text(2,0.2,'u')
ax.text(0.7,2.2,'v')

plt.grid('on')
plt.show()