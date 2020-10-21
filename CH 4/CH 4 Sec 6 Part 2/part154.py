#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:18:22 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [23,18]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca()

x = [0,3,3]
y = [0,1,2]
ax.fill(x,y,Color='g')

x = np.array([[0,3,3]])
y = np.array([[0,1,2]])
pts = np.concatenate((x,y),axis=0)
A = np.array([[np.cos(np.pi/2), -np.sin(np.pi/2)],
              [np.sin(np.pi/2), np.cos(np.pi/2)]])
Spts = A @ pts
ax.fill(Spts[0,:], Spts[1,:], Color='r')
ax.set_xlim(-3,3)
ax.set_ylim(0,4)
plt.grid('on')
plt.show()