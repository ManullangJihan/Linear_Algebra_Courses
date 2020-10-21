#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:08:07 2020

@author: hanjiya
"""

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()

ax.arrow(0,0,3,1,Color='b',LineWidth=1)
ax.arrow(0,0,1,2,Color='b',LineWidth=1)
ax.arrow(1,2,2,-1,Color='m',LineWidth=3)
ax.arrow(0,0,-1,-2,Color='r',LineWidth=1)
ax.arrow(0,0,2,-1,Color='r',LineWidth=1)
ax.plot([3,2],[1,-1],'--',Color='r')
ax.plot([-1,2],[-2,-1],'--',Color='r')
ax.text(3.1,1.1,'u = (3,1)')
ax.text(1.1,2.1,'v = (1,2)')
ax.text(-1.3,-2.3,'-v =(-1,-2)')
ax.text(2.1,-1.1,'u-v = (2,-1)')

plt.grid('on')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.axhline(0,Color='k')
plt.axvline(0,Color='k')