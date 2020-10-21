#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:59:57 2020

@author: hanjiya
"""

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,2,2,Color='b',LineWidth=4)
ax.arrow(0,0,4,4,Color='r',LineWidth=2)
ax.text(2.1,2.1,'(2,2)')
ax.text(4.1,4.1,'(4,4)')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.axhline(0, color='black')
plt.axvline(0, color='black')


plt.show()