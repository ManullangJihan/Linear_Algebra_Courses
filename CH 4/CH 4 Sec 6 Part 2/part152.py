#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 09:58:58 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10,8]
plt.rcParams.update({'font.size':18})

# First Plot
x1 = [2,3,3,2]
y1 = [2,2,3,3]
fig = plt.figure()
ax = fig.gca()
ax.fill(x1,y1,Color='r')

# Second Plot
x = np.array([[2,3,3,2]])
y = np.array([[2,2,3,3]])
pts = np.concatenate((x,y,np.ones_like(x)),axis=0)
A = np.array([[1,0,-2],
              [0,1,-2],
              [0,0,1]])
Spts = A @ pts
ax.fill(Spts[0,:],Spts[1,:],Color='g')
ax.set_xlim(0,4)
ax.set_ylim(0,4)
plt.grid('on')

plt.show()
