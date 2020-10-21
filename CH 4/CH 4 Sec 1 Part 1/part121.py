#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:57:13 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,8]
plt.rcParams.update({'font.size' : 18})

t = np.linspace(-5,5,200)
x = 2 + 2*t
y = 3 - 3*t

fig = plt.figure()
ax = fig.gca()
ax.plot(x,y)
ax.plot(2,3,'.')
u = 8 + 8*t + 8*t**2
v = -3 + 3*t
ax.plot(u,v,Color='r')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.text(2.3,3.5,'(2,3')

plt.xticks(np.arange(-10,11))
plt.yticks(np.arange(-10,11))
plt.grid('on')

plt.show()