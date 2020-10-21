#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:03:29 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,17]
plt.rcParams.update({'font.size':18})

x = np.arange(1975,2003)
x = x.T
y = np.array([[13.94, 13.86, 14.11, 14.02, 14.09, 14.16, 14.22, 14.04, 14.25, 14.07,
               14.03, 14.12, 14.27, 14.29, 14.19, 14.37, 14.32, 14.14, 14.14,
               14.25, 14.37, 14.23, 14.40, 14.56, 14.32, 14.31, 14.46, 14.52]])
y = y.T

fig = plt.figure()
ax = fig.gca()
ax.plot(x,y,'ro',Color='m')

# Cara 1
a1 = x.copy().reshape(28,1)
a2 = np.ones_like(x).reshape(28,1)
A = np.concatenate((a1,a2),axis=1)
b = y.copy()
xhat, resid, rank, s = np.linalg.lstsq(A,b)
yf = xhat[0,0] * x + xhat[1,0]
ax.plot(x,yf)
plt.xlabel('year')
plt.ylabel('Temperature')
plt.title('Average Temperature versus the year')
plt.grid('on')
plt.show()


# Cara 2
fig = plt.figure()
ax = fig.gca()
p = np.polyfit(x,y,1)
u = x.copy()
v = np.polyval(p,u)
ax.plot(u,v)
ax.plot(x,y,'ro',Color='r')

plt.xlabel('year')
plt.ylabel('Temperature')
plt.title('Average Temperature versus the year')
plt.grid('on')
plt.show()

