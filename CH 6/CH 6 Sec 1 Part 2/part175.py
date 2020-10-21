#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:15:52 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca()

ax.arrow(0,0,-2,3,LineWidth=1,Color='r')
ax.arrow(0,0,4,1,LineWidth=1,Color='r')
ax.arrow(4,1,-6,2,Linewidth=1,Color='b')
t = np.linspace(np.arctan2(1,4),np.arctan2(3,-2))
ax.plot(np.cos(t),np.sin(t),Color='k',LineWidth=1)
ax.text(0.4,1.2,'theta')
ax.text(2,0.2,'||v||')
ax.text(-1.4,1.3,'||u||')
ax.text(0.7,2.5,'||u-v||')

ax.set_xlim(-3,5)
ax.set_ylim(-1,4)
plt.grid('on')
plt.show()