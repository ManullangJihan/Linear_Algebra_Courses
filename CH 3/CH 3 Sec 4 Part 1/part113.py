#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:27:59 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [24,16]
plt.rcParams.update({'font.size' : 18})

t = np.linspace(-6,6)
fig = plt.figure()
ax = fig.gca()

for k in range(-5,6):
    ax.plot(-2*k+t, k+t, '--', Color='m')
    ax.plot(k-2*t, k+t, '--', Color='m')
    
ax.plot(t,t,'-',Color='k')
ax.plot(-2*t,t,'-',Color='k')
ax.arrow(0,0,1,1,LineWidth=1,Color='b')
ax.arrow(0,0,-2,1,LineWidth=3,Color='b')
ax.arrow(0,0,3,2,LineWidth=1,Color='b')
ax.arrow(0,0,-1,5,LineWidth=2,Color='b')
ax.arrow(0,0,3,3,LineWidth=3,Color='r')
ax.arrow(0,0,-4,2,LineWidth=3,Color='r',alpha=0.8)
ax.plot(-1,5,'o',Color='k')

ax.set_xlim(-6,6)
ax.set_ylim(-6,6)

ax.text(1,0.5,'b_1',Color='b')
ax.text(-2,0.5,'b_2',Color='b')
ax.text(-1.1,5.5,'P',Color='b')
ax.text(3,2.5,'3b_1',Color='r')
ax.text(-4,1.5,'2b_2',Color='r')

plt.grid('on')