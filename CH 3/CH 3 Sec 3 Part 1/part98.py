#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:19:02 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,8]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.add_subplot(111)

t = np.linspace(-6,6)
for k in range(-6,7):
    x = 2*k - t
    y = k + 2*t
    ax.plot(x,y,'--',Color='r')
    
for k in range(-6,7):
    x = -k + 2*t
    y = 2*k + t
    ax.plot(x,y,'--',Color='r')

ax.arrow(0,0,2,1,LineWidth=2,Color='b')
ax.arrow(0,0,-1,2,LineWidth=2,Color='b')
ax.arrow(0,0,1,8,LineWidth=2,Color='b')
ax.arrow(0,0,4,2,LineWidth=1,Color='m')
ax.arrow(0,0,-3,6,LineWidth=1,Color='m')
ax.plot([-3,1,4],[6,8,2],'--',Color='m', LineWidth=2)

ax.text(2.2,0.8,'v_1=(2,1)')
ax.text(4.2,1.7,'2v_1')
ax.text(-2.7,2,'v_2=(-1,2)')
ax.text(-3.7,6,'3v_2')
ax.text(0.5,8.4,'2v_1+3v_2 = (1,8)')

plt.xlim(-6,6)
plt.ylim(-2,10)

plt.show()  