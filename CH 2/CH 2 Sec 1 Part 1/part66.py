#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:23:19 2020

@author: hanjiya
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,2*np.pi)
r = 2.8284
x = r*np.cos(t)
y = r*np.sin(t)
fig = plt.figure()
ax = fig.gca()
ax.plot(x,y)
ax.arrow(0,0,2,2,LineWidth=1)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel('x1 axis')
plt.ylabel('x2 axis')
ax.text(2.1,2.1, '(2,2)')
U = np.array([[2],[2]])
norm_U = np.linalg.norm(U)
print(norm_U)


