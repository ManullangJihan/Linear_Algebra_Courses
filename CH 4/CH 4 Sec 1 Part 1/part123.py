#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:06:04 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,8]
plt.rcParams.update({'font.size':18})

u1 = np.arange(-5,6)
u2 = np.arange(-5,6)
U1, U2 = np.meshgrid(u1,u2)

#
fig = plt.figure()
ax = fig.gca()
ax.plot(U1,U2)
plt.show()

#
fig = plt.figure()
ax = fig.gca()
ax.plot(U1.T,U2.T)
plt.show()

#
fig = plt.figure()
ax = fig.gca()
ax.plot(U1,U2,Color='k')
ax.plot(U1.T,U2.T,Color='k')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.show()

#
fig = plt.figure()
ax = fig.gca()
ax.plot(U1,U2,Color='k')
ax.plot(U1.T,U2.T,Color='k')
X1 = U1 - 2*U2
X2 = U1 + U2
ax.plot(X1,X2,'--',Color='r')
ax.plot(X1.T,X2.T,'--',Color='r')
ax.arrow(0,0,1,1,Color='b',LineWidth=2)
ax.arrow(0,0,-2,1,Color='b',LineWidth=2)

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.show()









