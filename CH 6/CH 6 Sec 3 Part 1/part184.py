#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:47:50 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,13]
plt.rcParams.update({'font.size':18})

y = np.array([[-1,-4]]).T
u = np.array([[2,1]]).T
proj = (np.dot(y.T,u) / np.dot(u.T,u) @ u.T).T

print(proj)

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,y[0,0],y[1,0],LineWidth=2,Color='b')
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=2,Color='b')
ax.text(-1.1,-4.4,'y=(-1,-4)')
ax.text(2.2,1.1,'u=(2,1)')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

plt.xticks(np.arange(-5,5))
plt.yticks(np.arange(-5,5))

plt.show()

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,y[0,0],y[1,0],LineWidth=2,Color='b')
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=2,Color='b')
t = np.linspace(-5/2,5/2)
x = 2*t
y = t
ax.plot(x,y,'-',Color='k')
ax.text(-1.1,-4.4,'y=(-1,-4)')
ax.text(2.2,1.1,'u=(2,1)')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

plt.xticks(np.arange(-5,5))
plt.yticks(np.arange(-5,5))

plt.show()

fig = plt.figure()
ax = fig.gca()
y = np.array([[-1,-4]]).T
u = np.array([[2,1]]).T
ax.arrow(0,0,y[0,0],y[1,0],LineWidth=2,Color='b')
ax.arrow(0,0,u[0,0],u[1,0],LineWidth=2,Color='b')
ax.arrow(0,0,proj[0,0],proj[1,0],LineWidth=2,Color='r')
ax.plot([proj[0,0],y[0,0]],[proj[1,0],y[1,0]],'--',Color='r')
t = np.linspace(-5/2,5/2)
xx = 2*t
yy = t
ax.plot(xx,yy,'-',Color='k')

ax.text(-1.1,-4.4,'y=(-1,-4)')
ax.text(2.2,1.1,'u=(2,1)')
ax.text(-3.6,-1.1,'proj_u v')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

plt.xticks(np.arange(-5,5))
plt.yticks(np.arange(-5,5))
plt.grid('on')
plt.show()

