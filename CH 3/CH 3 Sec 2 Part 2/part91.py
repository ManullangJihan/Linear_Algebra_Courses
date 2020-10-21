#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:19:45 2020

@author: hanjiya
"""

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()
ax.plot([-5,5],[-10/3,10/3],alpha=0.5)
ax.arrow(0,0,3,2,LineWidth=1,Color='b')
ax.plot(0,0,'o',Color='m')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(-5,5)
plt.ylim(-5,5)

plt.show()