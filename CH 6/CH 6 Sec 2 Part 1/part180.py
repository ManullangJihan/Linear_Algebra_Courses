#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:03:12 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,2,1,LineWidth=1,Color='r')
x = np.linspace(-5,5)
y = -2*x
ax.plot(x,y,Color='b')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.grid('on')
plt.show()

##
fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,2,1,LineWidth=8,Color='r')
t = np.linspace(-5,5)
x = -t
y = 2*t
ax.plot(x,y,Color='b')
ax.arrow(0,0,-1,2,LineWidth=8,Color='r')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.grid('on')
plt.show()