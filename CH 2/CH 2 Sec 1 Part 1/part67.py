#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:45:37 2020

@author: hanjiya
"""

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,2,2,Color='b',LineWidth=1)
ax.arrow(0,0,-2,2,Color='b',LineWidth=1)
ax.arrow(0,0,0,4,Color='b',LineWidth=1)
ax.plot([-2,0,2],[2,4,2],'--',Color='r')
ax.text(2.1,2.1,'(2,1)')
ax.text(-2.8,2.1,'(-2,2)')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel('x1-axis')
plt.ylabel('x2-axis')
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.show()