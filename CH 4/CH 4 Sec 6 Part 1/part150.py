#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:16:27 2020

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
ax1.set_xlim(0,7)
ax1.set_ylim(0,5)

x = np.array([[0, 2, 1]])
y = np.array([[1, 1, 3]])
S = np.array([[1,2],[0,1]])
pts = np.concatenate((x,y), axis=0)
Spts = S @ pts
ax2.fill(Spts[0,:],Spts[1,:],Color='g')
ax1.set_xlim(0,7)
ax1.set_ylim(0,5)