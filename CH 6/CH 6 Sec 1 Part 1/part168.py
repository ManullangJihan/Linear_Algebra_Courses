#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:09:16 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,18]
plt.rcParams.update({'font.size':18})

u = np.array([[3,4]]).T
fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=2,Color='b')
ax.text(3,4.2,'(3,4)')
ax.set_xlim(0,5)
ax.set_ylim(0,5)
plt.grid('on')
plt.show()

u = np.array([[3,4]]).T
fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=2,Color='b')
t = np.linspace(0,2*np.pi)
x = 5*np.cos(t)
y = 5*np.sin(t)
ax.plot(x,y)
ax.text(3,4.2,'(3,4)')
ax.set_xlim(-6,6)
ax.set_ylim(-6,6)
plt.grid('on')
plt.show()




