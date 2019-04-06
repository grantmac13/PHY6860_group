from numpy import *
import matplotlib.pyplot as plt
a = 10
n_t = 100
p = zeros((a+1, n_t))  # 2d arrays updated in loops
# changed second dim of p array to not be same as space dim
D = 2
xmin = -5
tmin = 0
dx = 1
dt = .01
deriv = (D*dt)/(dx**2)


# added the initial density profile for second commit
p[int(a/2 - 1), 0] = 1.
p[int(a/2), 0] = 1.
p[int(a/2 + 1), 0] = 1.


for n in range(1, n_t):
    for i in range(a+1):

        if i == 0:
            p[i, n] = p[i, n-1] + deriv*(p[i+1, n-1] - 2*p[i, n-1])
        if i == a:
            p[i, n] = p[i, n-1] + deriv*(p[i-1, n-1] - 2*p[i, n-1])
        else:
            p[i, n] = p[i, n-1] + deriv*(p[i+1, n-1] - 2*p[i, n-1] + p[i-1, n])
        print(p)



def density(x, t):
    return p[x, t]


def gaussian(x, t):
    sigma = sqrt(2*D*t)
    rho = 1./(sqrt(2*pi)*sigma**2)*exp(-x**2/(2*sigma**2))

    return rho


# arbitrary x definition with length matching p[i,j]
x_plot = linspace(-5., 5., num=11)

# arbitrary x definition with length large enough to be smooth-ish
x_gaussian = linspace(-5., 5., num=41)


# to match colors on a timestep
colors = ['b', 'g', 'r', 'k', 'm']
count = 0



for j in range(n_t):
    if j%20 == 0:  # plot every 20 timesteps
        count += 1
        plt.plot(x_plot, p[:, j], color=colors[count-1])  # match colors to read easier
        plt.plot(x_gaussian, gaussian(x_gaussian, j*dt), color=colors[count-1], linestyle='dashed', label='Gaussian fit for t='+str(dt*j))
        plt.ylim((0, 1.1))


# all five sets of plots on one canvas
plt.legend()

# getting weird result. Can Ben check?
plt.show()


