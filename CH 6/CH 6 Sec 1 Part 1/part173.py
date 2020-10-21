#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:04:32 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,18]
plt.rcParams.update({'font.size':18})

fig = plt.figure()
ax = fig.gca()
ax.plot(1,4,'ko',Color='r')
ax.plot(4,1,'ko',Color='r')
ax.plot([1,4],[4,1],Color='b')
ax.text(1,4.3,'(u_1,u_2)')
ax.text(4,0.7,'(v_1,v_2)')
ax.text(2.5,2.7,'d')
ax.set_xlim(-1,5)
ax.set_ylim(-1,5)

plt.grid('on')
plt.show()


fig = plt.figure()
ax = fig.gca()
ax.plot(1,4,'ko',Color='r')
ax.plot(4,1,'ko',Color='r')
ax.arrow(0,0,4,1,LineWidth=1,Color='r')
ax.arrow(0,0,1,4,LineWidth=1,Color='r')
ax.arrow(4,1,-3,3,LineWidth=1,Color='b')

ax.text(1,4.3,'(u_1,u_2)')
ax.text(4,0.7,'(v_1,v_2)')
ax.text(0.6,2,'\textbf u')
ax.text(2.5,2.7,' u-v')
ax.text(2,0.7,'v')

ax.set_xlim(-1,5)
ax.set_ylim(-1,5)

plt.grid('on')
plt.show()
