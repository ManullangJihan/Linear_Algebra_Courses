#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:14:54 2020

@author: hanjiya
"""

import numpy as np
from sympy import *
import matplotlib.pyplot as plt

t = Symbol('t')
x = Matrix([[3*t],[t+2]])
u = x.subs(t,2)
v = x.subs(t,3)
ans1 = x.subs(t,5)
print(u+v==ans1)

# Visualize Our Answer
fig = plt.figure()
t = np.linspace(-2,2,20)
x = 3*t
y = t+2
ax = fig.gca()
ax.plot(x,y,Color='b',LineWidth=1)
ax.arrow(0,0,-3,1,Color='r',LineWidth=2)
ax.arrow(0,0,3,3,Color='r',LineWidth=2)
ax.arrow(0,0,0,4,Color='r',LineWidth=2)
ax.plot([-3,0,3],[1,4,3],'--',Color='k',LineWidth=1)
ax.text(-3.4,1.3,'v1',FontSize=14)
ax.text(3.2,2.8,'v2',FontSize=14)
ax.text(0,4.3,'v1+v2',FontSize=14)

plt.xlim(-4,4)
plt.ylim(-1,6)
plt.grid('on')

plt.show()
