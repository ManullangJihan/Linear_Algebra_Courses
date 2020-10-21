#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:54:14 2020

@author: hanjiya
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,8]
plt.rcParams.update({'font.size':18})

#
x = np.arange(-10,10)
y = -3/2 * x + 6

fig = plt.figure()
ax = fig.gca()

ax.plot(x,y)
ax.plot(2,3,'.',MarkerSize=15)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.text(2.3,3.3,'(2,3)')
plt.xticks(np.arange(-10,10))
plt.yticks(np.arange(-10,10))
plt.grid('on')
plt.show()

# Now, let's recall the parallelogram method for adding two vectors.
fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,1,2,LineWidth=1,Color='b')
ax.arrow(0,0,5,3,LineWidth=1,Color='b')
ax.arrow(0,0,4,1,LineWidth=1,Color='b')
ax.plot([1,5,4],[2,3,1],'--',Color='r')
ax.text(0.5,1,'u',FontSize=14);
ax.text(3,1.8,'u+v',FontSize=14);
ax.text(3,0.8,'v',FontSize=14);
plt.grid('on')
plt.show()

# Note that the sides of the parallelogram are parallel 
# and the same length, so another way of adding two vectors ?u and ?v 
# geometrically is to add the beginning of vector ?v 
# to the tip of vector ?u, then draw the vector ?u+?v by beginning 
# at the base of ?u and ending at tip of vector ?v.

fig = plt.figure()
ax = fig.gca()
ax.arrow(0,0,1,2,LineWidth=1,Color='r')
ax.arrow(0,0,5,3,LineWidth=1,Color='r')
ax.arrow(1,2,4,1,LineWidth=1,Color='r')
ax.text(0.5,1,'u',FontSize=14)
ax.text(2.5,1.5,'u+v',FontSize=14)
# ax.text(3,2.5,1,'v',FontSize=14)
plt.show()

# We will find this extremely useful. Now, let's draw our line 
# y=(?3/2)x+6 again, but this time add some vectors to our image.
x = np.arange(-10,11)
y = -3/2*x+6
fig = plt.figure()
ax = fig.gca()
ax.plot(x,y)
ax.plot(2,3,'.',MarkerSize=16)
ax.arrow(0,0,2,3,Color='r')
ax.arrow(2,3,2,-3,Color='r')
ax.arrow(0,0,8,-6,Color='r')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.text(2.3,3.5,'(2,3)')
ax.text(8.5,-6,'(x,y)')
ax.text(3,1.5,'v')
ax.text(1,1.5,'p_0')
ax.text(4,-3,'p')
plt.xticks(np.arange(-10,11))
plt.yticks(np.arange(-10,11))
plt.show()

#
t = np.linspace(-5,5)
x = 2 + 2*t
y = 3 - 3*t
fig = plt.figure()
ax = fig.gca()
ax.plot(x,y)
ax.plot(2,3,'.',MarkerSize=15)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.text(2.3,3.5,'(2,3)')
plt.xticks(np.arange(-10,11))
plt.yticks(np.arange(-10,11))
plt.grid('on')
plt.show()

#
fig = plt.figure()
ax = fig.gca()
t = np.linspace(-5,5)
x = 2 + 2*t
y = 3 - 3*t
ax.plot(x,y)
ax.plot(2,3,'.',MarkerSize=16)
u = 8 - 4*t
v = 12*t
ax.plot(u,v,Color='r')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.text(2.3,3.5,'(2,3)')
plt.xticks(np.arange(-10,11))
plt.yticks(np.arange(-10,11))
plt.grid('on')
plt.show()