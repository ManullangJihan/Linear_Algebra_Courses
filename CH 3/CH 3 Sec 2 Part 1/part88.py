#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:41:23 2020

@author: hanjiya
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:40:09 2020

@author: hanjiya
"""

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca()
ax.fill([0,5,5,0,0],[0,0,-5,-5,0],Color='r',alpha=0.1)
ax.fill([0,-5,-5,0,0],[0,0,5,5,0],Color='r',alpha=0.1)
ax.arrow(0,0,2,-1,Color='b',LineWidth=1)
ax.arrow(0,0,-4,2,Color='r',LineWidth=1)
ax.plot(0,0,'o',MarkerFaceColor='k')
ax.text(2,-1.2,'u = (2,-1)')
ax.text(-4,2.2,'u = (-4,2)')
plt.grid('on')
plt.show()

# How if we multiply by 2 using u = (2,-1) & v = (4,-2)

fig = plt.figure()
ax = fig.gca()
ax.fill([0,5,5,0,0],[0,0,-5,-5,0],Color='r',alpha=0.1)
ax.fill([0,-5,-5,0,0],[0,0,5,5,0],Color='r',alpha=0.1)
ax.arrow(0,0,2,-1,Color='b',LineWidth=1)
ax.arrow(0,0,4,-2,Color='r',LineWidth=1)
ax.plot(0,0,'o',MarkerFaceColor='k')
ax.text(2,-1.2,'u = (2,-1)')
ax.text(-4,2.2,'u = (-4,2)')
plt.grid('on')
plt.show() 

# How if u = (2,-1) and v = (-1,3) and we add both of them by z = (1,2)
fig = plt.figure()
ax = fig.gca()
ax.fill([0,5,5,0,0],[0,0,-5,-5,0],Color='r',alpha=0.1)
ax.fill([0,-5,-5,0,0],[0,0,5,5,0],Color='r',alpha=0.1)
ax.arrow(0,0,2,-1,Color='b',LineWidth=1)
ax.arrow(0,0,-1,3,Color='r',LineWidth=1)
ax.arrow(0,0,1,2,Color='r',LineWidth=1)
ax.plot([-1,1,2],[3,2,-1],'--',Color='r')
ax.plot(0,0,'o',MarkerFaceColor='k')
ax.text(2,-1.2,'u = (2,-1)')
ax.text(-4,2.2,'u = (-4,2)')
ax.text(1,2.2,'u+v =(1,2)')
plt.grid('on')
plt.show()



