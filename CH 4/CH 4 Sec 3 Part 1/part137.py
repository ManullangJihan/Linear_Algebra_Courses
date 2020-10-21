#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:35:10 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,Matrix

plt.rcParams['figure.figsize'] = [24,18]
plt.rcParams.update({'font.size': 18})

a,b,c = symbols('a,b,c')
A = Matrix([[1,1,2,a],[1,2,3,b],[1,1,2,c]])
r1 = A[0,:]
r2 = A[1,:]
r3 = A[2,:]
A = Matrix([r1,r2-r1,r3-r1])
print(A)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

x = 1 - 2*np.random.rand(1,100)
y = 1 - 2*np.random.rand(1,100)
z = 1 - 2*np.random.rand(1,100)
b = np.linspace(-8,8,20)
c = np.linspace(-8,8,20)
B,C = np.meshgrid(b,c)
X = C
Y = B
Z = C
ax.plot_surface(X,Y,Z,EdgeColor='green',alpha=0.1)
pts = np.concatenate((x,y,z),axis=0)
A = np.array([[1,1,2],[1,2,3],[1,1,2]])
Tpts = A @ pts
ax.scatter3D(Tpts[0,:], Tpts[1,:], Tpts[2,:],Color='b')

# They all lie on our plane, so this is clear visual evidence that 
# this linear transformation is not onto all of R^3 .