#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:11:42 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,8]
plt.rcParams.update({'font.size' : 18})

fig = plt.figure()
ax = fig.add_subplot(111)
ax.arrow(0,0,1,0,LineWidth=2,Color='b')
ax.arrow(0,0,0,1,LineWidth=2,Color='b')
ax.arrow(0,0,3,0,LineWidth=1,Color='r')
ax.arrow(0,0,0,4,LineWidth=1,Color='r')
ax.arrow(0,0,3,4,LineWidth=1,Color='r')
ax.plot([0,3,3],[4,4,0],'--',Color='r')

a = 3
b = 4

ax.text(1,-0.4,'e_1')
ax.text(a,-0.4,'3e_1')
ax.text(-0.4,1,'e_2')
ax.text(-0.4,b,'4e_2')
ax.text(a,b+0.2,'3e_1+4e_2')

plt.xlim(-1,5)
plt.ylim(-1,5)

plt.show()