from numpy import *
import matplotlib.pyplot as plt
a = 10
p = zeros((a+1, a+1))  # 2d arrays updated in loops
D = 2
xmin = -2.5
tmin = 0
dx = .5
dt = .01
deriv = (D*dt)/(dx**2)

def gaussian(x, t):
    sigma = sqrt(2*D*t)
    rho = 1./(sqrt(2*pi)*sigma**2)*exp(-x**2/(2*sigma**2))

    return rho

def density(x, t):
    return (4*pi*D*t)**((x**2)/(8*D*t))


x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []


for n in range(a+1):
    for i in range(a+1):
        if n == 0:
            p[i, n] = density(xmin + i*dx, 0.01)
        else:
            if i == 0:
                p[i, n] = p[i, n - 1] + deriv * (p[i + 1, n - 1] - 2 * p[i, n - 1])
            if i == a:
                p[i, n] = p[i, n - 1] + deriv * (p[i - 1, n - 1] - 2 * p[i, n - 1])
            else:
                p[i, n] = p[i, n - 1] + deriv * (p[i + 1, n - 1] - 2 * p[i, n - 1] + p[i - 1, n])
        x = xmin + i*dx
        if n == a / 5:
            x1.append(x)
            p1.append(p[i, n])
        elif n == a * .4:
            x2.append(x)
            p2.append(p[i, n])
        elif n == a * .6:
            x3.append(x)
            p3.append(p[i, n])
        elif n == a * .8:
            x4.append(x)
            p4.append(p[i, n])
        elif n == a:
            x5.append(x)
            p5.append(p[i, n])
plt.plot(x1, p1, 'b*')
plt.xlabel("position")
plt.ylabel("density")
plt.title("1D diffusion density after 0.02 seconds")
plt.show()
plt.plot(x2, p2, 'k*')
plt.xlabel("position")
plt.ylabel("density")
plt.title("1D diffusion density after 0.04 seconds")
plt.show()
plt.plot(x3, p3, 'g*')
plt.xlabel("position")
plt.ylabel("density")
plt.title("1D diffusion density after 0.06 seconds")
plt.show()
plt.plot(x4, p4, 'c*')
plt.xlabel("position")
plt.ylabel("density")
plt.title("1D diffusion density after 0.08 seconds")
plt.show()
plt.plot(x5, p5, 'r*')
plt.xlabel("position")
plt.ylabel("density")
plt.title("1D diffusion density after 0.1 seconds")
plt.show()

plt.plot(x_gaussian, gaussian(x_gaussian, j*dt), color=colors[count-1], linestyle='dashed', label='Gaussian fit for t='+str(dt*j))


