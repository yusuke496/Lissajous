from numpy import sin,pi,linspace
from matplotlib import pyplot as plt

t = linspace(-pi,pi,10000)
delta = 1
a = 1
b = 1
L1= 1
L2= 1

x = L1*sin(a * t + delta)
y = L2*sin(b * t)

plt.scatter(x,y, marker='.', color='black', s=0.5)
plt.subplot().set_aspect('equal')
plt.show()
