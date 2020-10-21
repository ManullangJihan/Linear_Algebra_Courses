#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:18:53 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-6,6)
fig = plt.figure()
ax = fig.gca()

for k in range(-6,7):
    x = -k + 2*t
    y = k + t
    ax.plot(x,y,'--',Color='r',LineWidth=0.5)

for k in range(-3,4):
    x = 2*k - t
    y = k + t
    ax.plot(x,y,'--',Color='r',LineWidth=0.5)

ax.arrow(0,0,2,1,Color='b',LineWidth=1)
ax.arrow(0,0,-1,1,Color='b',LineWidth=1)
ax.arrow(0,0,4,2,Color='m',LineWidth=1)
ax.arrow(0,0,-3,3,Color='m',LineWidth=1)
ax.arrow(0,0,1,5,Color='b',LineWidth=1)
ax.plot([4,1],[2,5],'--',Color='m', LineWidth=2)
ax.plot([-3,1],[3,5],'--',Color='m', LineWidth=2)

ax.text(2.2,0.8,'v_1=(2,1)')
ax.text(4.2,1.7,'2v_1')
ax.text(-2.5,0.8,'v_2=(-1,1)')
ax.text(-3.7,2.8,'3v_2')
ax.text(0.5,5.2,'2v_1+3v_2')

plt.xlim(-6,6)
plt.ylim(-6,6)