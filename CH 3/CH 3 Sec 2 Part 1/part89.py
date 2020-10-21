#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:56:14 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

#
t = np.linspace(-3,3)
x = 1+2*t
y = 3 - 2*t
fig = plt.figure()
ax = plt.gca()
ax.plot(x,y)
plt.xlim(-2,6)
plt.ylim(-2,6)
plt.grid('on')

#
t = np.linspace(-3,3)
x = 1+2*t
y = 3 - 2*t
fig = plt.figure()
ax = plt.gca()
ax.plot(x,y)
ax.plot(1,3,'o',MarkerFaceColor='m')
ax.plot(3,1,'o',MarkerFaceColor='m')
ax.plot(0,0,'o',MarkerFaceColor='m')
ax.arrow(0,0,1,3,Color='b',LineWidth=1)
ax.arrow(0,0,3,1,Color='b',LineWidth=1)
ax.arrow(0,0,4,4,Color='m',LineWidth=1)
ax.plot([1,4,3],[3,4,1],'--',Color='r')
ax.text(1.2,3.2,'(1,3)')
ax.text(3.2,1.2,'(3,1)')
ax.text(4.1,4.1,'(4,4)')

plt.xlim(-2,6)
plt.ylim(-2,6)
plt.grid('on')

plt.show()