from numpy import *
import matplotlib.pyplot as plt
a = 10
p = zeros((a+1, a+1))  # 2d arrays updated in loops
D = 2
xmin = -5
tmin = 0
dx = 1
dt = .01
deriv = (D*dt)/(dx**2)


for n in range(a+1):
    if n == 0:
        n = 0 # initial condition
    for i in range(a+1):

        if i == 0:
            p[i, n] = p[i, n-1] + deriv*(p[i+1, n-1] - 2*p[i, n-1])
        if i == a:
            p[i, n] = p[i, n - 1] + deriv * (p[i - 1, n - 1] - 2 * p[i, n - 1])
        else:
            p[i, n] = p[i, n - 1] + deriv * (p[i + 1, n - 1] - 2 * p[i, n - 1] + p[i-1, n])


def density(x, t):
    return p[x, t]



