#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:50:34 2020

@author: hanjiya
"""

from sympy import Matrix, symbols
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,8]
plt.rcParams.update({'font.size' : 18})

x,y = symbols('x,y')
A = Matrix([[2,4],[3,6]])
sys = Matrix([[x,y]]).T
T = A @ sys
T_1 = T.subs([(x,1),(y,0)])
T_2 = T.subs([(x,0),(y,1)])

print(T_1)
print(T_2)

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,2,4,Color='r',LineWidth=4)
ax.arrow(0,0,3,6,Color='b',LineWidth=1, alpha=0.8)
ax.set_xlim(0,5)
ax.set_ylim(0,7)

plt.grid('on')
plt.show()
