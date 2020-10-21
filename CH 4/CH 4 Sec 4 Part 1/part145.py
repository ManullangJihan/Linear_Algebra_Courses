#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 07:54:28 2020

@author: hanjiya
"""

from sympy import Matrix
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [24,16]
plt.rcParams.update({'font.size':18})

A = Matrix([[1,1],[2,-1]])
b1 = Matrix([[-1,1]]).T
b2 = Matrix([[2,1]]).T
c1 = Matrix([[-2,1]]).T
c2 = Matrix([[1,1]]).T
Tb1 = A @ b1
Tb2 = A @ b2
M = c1.col_insert(1,c2).col_insert(2,Tb1).col_insert(3,Tb2)
Mref, Mpiv = M.rref()
TCB = Mref[:,[2,3]]
print(Mref)
print(TCB)

fig = plt.figure()
ax = fig.gca()
t = np.linspace(-10,10)

for k in range(-10,11):
    ax.plot(-k+2*t, k+t, '--', Color='r')
    ax.plot(2*k-t, k+t, '--', Color='r')

ax.arrow(0,0,2,1,LineWidth=4,Color='r')
ax.arrow(0,0,-1,1,LineWidth=4,Color='r')
ax.arrow(0,0,4,2,LineWidth=2,Color='b')
ax.arrow(0,0,-2,2,LineWidth=2,Color='b')
ax.arrow(0,0,2,4,LineWidth=2,Color='b')
ax.plot([-2,2,4],[2,4,2],'--',Color='r')
ax.text(-1.5,0.8,'b_1')
ax.text(-2.7,1.8,'2b_1')
ax.text(2,0.5,'b_2')
ax.text(4,1.5,'2b_2')
ax.text(2,4.5,'v=(2,4) and [v]_B=(2,2)')
ax.set_xlim(-4,6)
ax.set_ylim(-4,6)
plt.grid('on')
plt.show()


fig = plt.figure()
ax = fig.gca()
t = np.linspace(-10,10)

for k in range(-10,11):
    ax.plot(k-2*t, k+t, '--', Color='r')
    ax.plot(-2*k+t, k+t, '--', Color='r')

ax.arrow(0,0,4,-2,LineWidth=2,Color='b')
ax.arrow(0,0,2,2, LineWidth=2,Color='b')
ax.arrow(0,0,6,0, LineWidth=2,Color='b')
ax.arrow(0,0,-2,1, LineWidth=4,Color='r')
ax.arrow(0,0,1,1, LineWidth=4,Color='r')

ax.text(-2,1.3,'c_1')
ax.text(4,-2.4,'-2c_1')
ax.text(1,0.6,'c_2')
ax.text(2,2.4,'2c_2')
ax.text(6,1,'T(v)=(6,0)')
ax.text(6,-1,'[T(v)]_C=(-2,2)')


ax.set_xlim(-3,9)
ax.set_ylim(-5,5)
plt.xticks(np.arange(-3,9))
plt.yticks(np.arange(-5,5))
plt.grid('on')
plt.show()
