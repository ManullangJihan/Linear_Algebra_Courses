#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:35:52 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca()

u = np.array([[3,2]]).T
v = np.array([[-2,3]]).T
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=1,Color='b')
ax.arrow(0,0,v[0,0],v[1,0],LineWidth=1,Color='b')
t = np.linspace(np.arctan2(2,3),np.arctan2(3,-2))
ax.plot(np.cos(t),np.sin(t),Color='k',LineWidth=2)

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.text(3.1,2,'(3,2)')
ax.text(-2,3.3,'(-2,3)')
ax.text(0.2,1.2,'theta')
ax.text(1.5,0.8,'u')
ax.text(-1.1,1.2,'v')

plt.grid('on')
plt.show()

check_orthogonal = np.dot(u.T,v)/np.linalg.norm(u)*np.linalg.norm(v) == 0
print(check_orthogonal)