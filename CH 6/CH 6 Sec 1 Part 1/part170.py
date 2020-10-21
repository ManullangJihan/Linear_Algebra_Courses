#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 06:00:37 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,18]
plt.rcParams.update({'font.size':18})

u = np.array([[1,3,-2]]).T
norm_u = np.linalg.norm(u)**2
dot_u = np.dot(u.T,u)
print(norm_u == dot_u)


# Part 2
u = np.array([[2,1]]).T
v = 2*u
w = -2*u

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=3,Color='r')
ax.arrow(0,0,v[0,0],v[1,0],LineWidth=1,Color='b')
ax.arrow(0,0,w[0,0],w[1,0],LineWidth=1,Color='b')

ax.text(2,0.5,'u')
ax.text(4,1.5,'v')
ax.text(-4,-2.5,'w')

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

plt.grid('on')
plt.show()