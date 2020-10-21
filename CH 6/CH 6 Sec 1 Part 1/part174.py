#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:10:04 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,18]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,-2,3,LineWidth=1,Color='b')
ax.arrow(0,0,3,1,LineWidth=1,Color='b')
ax.arrow(3,1,-5,2,LineWidth=1,Color='r')
ax.plot(-2,3,'ko',Color='r')
ax.plot(3,1,'ko',Color='r')

ax.text(3,1.3,'(3,1)')
ax.text(-2,3.3,'(-2,3)')
ax.text(-1.3,1.4,'u')
ax.text(1.5,0.35,'v')
ax.text(0.7,2.2,'u-v')

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.grid('on')
plt.show()

u = np.array([[-2,3]]).T
v = np.array([[3,1]]).T
norm_u_min_v = np.linalg.norm(u-v)
print(norm_u_min_v)