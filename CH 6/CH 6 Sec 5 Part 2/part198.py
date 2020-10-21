#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:10:59 2020

@author: hanjiya
"""

from sympy import Matrix, ones, zeros
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [20,17]
plt.rcParams.update({'font.size':18})

x = Matrix([[-2,-1,1,2]]).T
y = Matrix([[3,2,1,2]]).T
x1 = zeros(4,1)

for i in range(x.shape[0]):
    x1[i,0] = x[i,0]**2

xhat = x1.col_insert(1,x).col_insert(2,ones(4,1))
b1 = xhat.T @ xhat
b2 = xhat.T @ y
abc = b1.col_insert(4, b2)
abc, piv = abc.rref()


fig = plt.figure()
ax = fig.gca()
ax.plot(x.T,y.T,'o',Color='r')
x2 = np.linspace(-3,3,100)
x2 = x2.reshape(1,100)
y11 = np.array([abc[0,3]*x2**2])
y12 = np.array([abc[1,3] * x2 + abc[2,3]])
y1 = np.array([y11+y12])
y1 = y1.reshape(1,100)
y1 = y1.astype('float64')
ax.plot(x2,y1,'-',Color='b',LineWidth=3)
plt.title('Best fit polynomial')
plt.grid('on')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

# Cara Kedua
x = [-2,-1,1,2]
y = [3,2,1,2]
fig = plt.figure()
ax = fig.gca()
ax.plot(x,y,'ro',Color='m')
p = np.polyfit(x,y,2)
u = np.linspace(-3,3,100)
v = np.polyval(p,u)
ax.plot(u,v)
plt.title('Best fit polynomial')
plt.grid('on')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()