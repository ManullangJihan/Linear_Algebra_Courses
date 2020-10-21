#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:07:13 2020

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
ax1.set_xlim(-1,3)
ax1.set_ylim(-1,3)

x = np.array([[0,2,1]])
y = np.array([[1,1,3]])
pts = np.concatenate((x,y), axis=0)
S = np.array([[1,0],[0,1/3]])
Spts = S @ pts
ax2.fill(Spts[0,:],Spts[1,:], Color='g')
ax2.set_xlim(-1,3)
ax2.set_ylim(-1,3)

plt.show()
