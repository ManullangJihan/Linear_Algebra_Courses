#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:05:38 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10,8]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca()

x1 = [2,4,3]
y1 = [2,2,4]
ax.fill(x1,y1,Color='g')
x2 = [1,2,3/2]
y2 = [1,1,5]
ax.fill(x2,y2,Color='r')
ax.set_xlim(0,4)
ax.set_ylim(0,5)
plt.grid('on')
plt.show()

fig = plt.figure()
ax = fig.gca()
x = [2,4,3]
y = [2,2,4]
ax.fill(x,y,Color='g')
x = np.array([[2,4,3]])
y = np.array([[2,2,4]])
pts = np.concatenate((x,y,np.ones_like(x)),axis=0)
A = np.array([[1,0,-2],
              [0,1,-2],
              [0,0,1]])
Spts = A @ pts
ax.fill(Spts[0,:],Spts[1,:],Color='r')
ax.set_xlim(0,4)
ax.set_ylim(0,5)
plt.grid('on')
plt.show()

#
fig = plt.figure()
ax = fig.gca()
x = [2,4,3]
y = [2,2,4]
ax.fill(x,y,Color='g')
x = np.array([[2,4,3]])
y = np.array([[2,2,4]])
pts = np.concatenate((x,y,np.ones_like(x)),axis=0)
A = np.array([[1,0,-2],
              [0,1,-2],
              [0,0,1]])
Spts = A @ pts
ax.fill(Spts[0,:],Spts[1,:],Color='r')
B = np.array([[1/2,0,0],
              [0,2,0],
              [0,0,1]])
Bpts = B @ Spts
ax.fill(Bpts[0,:],Bpts[1,:],Color='b')
ax.set_xlim(0,4)
ax.set_ylim(0,5)
plt.grid('on')
plt.show()

#
fig = plt.figure()
ax = fig.gca()
x = [2,4,3]
y = [2,2,4]
ax.fill(x,y,Color='g')
x = np.array([[2,4,3]])
y = np.array([[2,2,4]])
pts = np.concatenate((x,y,np.ones_like(x)),axis=0)
A = np.array([[1,0,-2],
              [0,1,-2],
              [0,0,1]])
Spts = A @ pts
ax.fill(Spts[0,:],Spts[1,:],Color='r')
B = np.array([[1/2,0,0],
              [0,2,0],
              [0,0,1]])
Bpts = B @ Spts
ax.fill(Bpts[0,:],Bpts[1,:],Color='b')
C = np.array([[1,0,1],
              [0,1,1],
              [0,0,1]])
Cpts = C @ Bpts
ax.fill(Cpts[0,:],Cpts[1,:],Color='y')
ax.set_xlim(0,4)
ax.set_ylim(0,5)
plt.grid('on')
plt.show()

#
fig = plt.figure()
ax = fig.gca()
x = [2,4,3]
y = [2,2,4]
ax.fill(x,y,Color='g')
CBA = C @ B @ A
x = np.array([[2,4,3]])
y = np.array([[2,2,4]])
pts = np.concatenate((x,y,np.ones_like(x)),axis=0)
Spts = CBA @ pts
ax.fill(Spts[0,:],Spts[1,:],Color='r')
ax.set_xlim(0,4)
ax.set_ylim(0,5)
plt.grid('on')
plt.show()