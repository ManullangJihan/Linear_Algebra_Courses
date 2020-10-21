#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:50:03 2020

@author: hanjiya
"""

from sympy import Matrix
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [24,16]
plt.rcParams.update({'font.size':24})

A = Matrix([[2,-1,1,0],
            [1,1,0,1]])
M, piv = A.rref()
PBE = M[:,[2,3]]
v = Matrix([[1],[5]])
V = PBE @ v
print(V)

C = Matrix([[1,-3,2,-1],[1,1,1,1]])
Crowred, pivC = C.rref()
PBE2 = Crowred[:,[2,3]]
V2 = PBE2 @ V
print(V2)

# Visualize Our Answer
fig = plt.figure()
ax = fig.gca()

t = np.linspace(-5,5)

for k in range(-5,6):
    ax.plot(2*k-t,k+t,'--',Color='r')
    ax.plot(-k+2*t,k+t,'--',Color='r')
    
ax.plot(2*t,t,Color='k')
ax.plot(-t,t,Color='k')

ax.arrow(0,0,2,1,LineWidth=2,Color='b')
ax.arrow(0,0,-1,1,LineWidth=2,Color='b')
ax.arrow(0,0,4,2,LineWidth=1,Color='r')
ax.arrow(0,0,-3,3,LineWidth=1,Color='r')
ax.arrow(0,0,1,5,LineWidth=2,Color='r')
ax.plot([-3,1,4],[3,5,2],'--',LineWidth=2,Color='k')
ax.plot(1,5,'o',Color='y')

ax.text(2,0.7,'b_1',Color='b')
ax.text(-1.2,0.7,'b_2',Color='b')
ax.text(4.3,1.9,'2b_1',Color='r')
ax.text(-3.5,3,'3b_2',Color='r')
ax.text(1.1,5.5,'(1,5)')

ax.set_xlim(-5,5)
ax.set_ylim(-1,6)
plt.grid('on')

# Visualize 2
fig = plt.figure()
ax = fig.gca()

t = np.linspace(-5,5)
for k in range(-5,6):
    ax.plot(k-3*t,k+t,'--',Color='r')
    ax.plot(-3*k+t,k+t,'--',Color='r')

ax.plot(-3*t,t,'k')
ax.plot(t,t,'k')
ax.arrow(0,0,-3,1,LineWidth=2,Color='b')
ax.arrow(0,0,1,1,LineWidth=2,Color='b')
ax.arrow(0,0,1,5,LineWidth=2,Color='r')
ax.arrow(0,0,4,4,LineWidth=1,Color='r')
ax.arrow(0,0,-3,1,LineWidth=1,Color='r')
ax.plot([-3,1,4],[1,5,4],'--',Color='k',LineWidth=2)
ax.plot(1,5,'o','y')

ax.text(1.2,0.9,'c_1',Color='b')
ax.text(-3.4,0.9,'c_2',Color='b')
ax.text(4.2,3.9,'4c_1',Color='r')
ax.text(-3.5,1.3,'1c_2',Color='r')
ax.text(1,5.3,'(1,5)',Color='k')

ax.set_xlim(-5,5)
ax.set_ylim(-1,6)

plt.grid('on')
plt.show()