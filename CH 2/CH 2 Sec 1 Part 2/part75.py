#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:13:44 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sympy import *

A = np.array([[1,1,2,1],[-2,0,1,-3],[1,1,2,1]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,r2+2*r1,r3-r1])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1,0.5*r2,r2])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = np.array([r1-r2,r2,r3])
print(A)

# Cara 2
A = Matrix([[1,1,2,1],[-2,0,1,-3],[1,1,2,1]])
A_ref_matrix, A_ref_pivot = A.rref()
print(A_ref_matrix)

# Visualisasi
t = np.linspace(-1,1)
x = 3/2 * t +3/2
y = 5/2 * t -1/2
z = t
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot(x,y,z,Color='b',LineWidth=3)
plt.xlabel('c1-axis')
plt.ylabel('c2-axis')
plt.grid('on')

plt.show()
