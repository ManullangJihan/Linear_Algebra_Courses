#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:06:06 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,17]
plt.rcParams.update({'font.size':18})

x = np.array([[-2,-1,1,2]]).T
y = np.array([[-1,0,1,2]]).T
fig = plt.figure()
ax = fig.gca()
ax.plot(x,y,'o',Color='r')
b = np.ones((4,1))
mb = np.concatenate((x,b),axis=1)
m = np.linalg.inv(mb.T @ mb) @ mb.T @ y
x1 = np.linspace(-3,3)
yf = m[0,0] * x1 + m[1,0]
ax.plot(x1,yf)

ax.set_xlim(-3,3)
ax.set_ylim(-2,2.5)
plt.grid('on')
plt.show()

# Calculate Error
err = (y-yf)**2
print(err)