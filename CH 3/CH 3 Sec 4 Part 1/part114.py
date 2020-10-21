#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:38:56 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [24,16]
plt.rcParams.update({'font.size' : 18})

fig = plt.figure()
ax = fig.gca()

t = np.linspace(-6,6)
for k in range(-5,6):
    ax.plot(-2*k+t, k+t, '--', Color='m')
    ax.plot(k-2*t, k+t, '--', Color='m')
    
ax.plot(t,t,'-',Color='k')
ax.plot(-2*t, t, '-', Color='k')
ax.arrow(0,0,1,1,LineWidth=2, Color='b')
ax.arrow(0,0,-2,1,LineWidth=2, Color='b')
ax.arrow(0,0,-1,-4,LineWidth=2, Color='b')
ax.arrow(0,0,-3,-3,LineWidth=1, Color='r')
ax.arrow(0,0,2,-1,LineWidth=1, Color='r')
ax.plot([-3,-1,2],[-3,-4,-1],'--',Color='r', LineWidth=2)
ax.plot(-1,-4,'o',Color='k')

ax.text(1,0.5,'b_1',Color='b')
ax.text(-2,0.5,'b_2',Color='b')
ax.text(-1.1,-4.5,'P',Color='b')
ax.text(-3,-3.5,'-3b_1',Color='r')
ax.text(2,-1.4,'-1b_2',Color='r')

ax.set_xlim(-6,6)
ax.set_ylim(-6,6)

plt.grid('on')

plt.show()