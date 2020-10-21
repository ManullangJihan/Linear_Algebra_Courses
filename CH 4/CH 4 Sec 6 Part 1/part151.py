#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:21:59 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,8]
plt.rcParams.update({'font.size':18})

x = [0, 2, 1]
y = [1, 1, 3]

fig, (ax1,ax2) = plt.subplots(2,1)
ax1.fill(x,y, Color='g')
ax1.set_xlim(0,5)
ax1.set_ylim(0,5)

x = np.array([[0, 2, 1]])
y = np.array([[1, 1, 3]])
S = np.array([[0,1],[1,0]])
pts = np.concatenate((x,y), axis=0)
Spts = S @ pts
ax2.fill(Spts[0,:],Spts[1,:],Color='g')
ax1.set_xlim(0,5)
ax1.set_ylim(0,5)

plt.show()

# 
x = [0, 2, 1]
y = [1, 1, 3]

fig = plt.figure()
ax = plt.gca()
ax.fill(x,y, Color='m', alpha=0.2)
ax.plot([-5,5],[-5,5], LineWidth=2, Color='b')
x = np.array([[0, 2, 1]])
y = np.array([[1, 1, 3]])
S = np.array([[0,1],[1,0]])
pts = np.concatenate((x,y), axis=0)
Spts = S @ pts
ax.fill(Spts[0,:],Spts[1,:],Color='g', alpha=0.2)
ax.set_xlim(0,5)
ax.set_ylim(0,5)

plt.grid('on')
plt.show()