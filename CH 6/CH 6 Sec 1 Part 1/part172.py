#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:59:57 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,18]
plt.rcParams.update({'font.size':18})

v = np.array([[2,2,]]).T
u = v / np.linalg.norm(v)

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,v[0,0],v[1,0], LineWidth=1, Color='b')
ax.arrow(0,0,u[0,0],u[1,0], LineWidth=2, Color='r')
t = np.linspace(0,2*np.pi)
x = np.cos(t)
y = np.sin(t)
ax.plot(x,y)

ax.text(0.8,0.6,'u')
ax.text(2.1,1.8,'v')

ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
plt.grid('on')

plt.show()