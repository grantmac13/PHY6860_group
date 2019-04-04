import numpy as np
import matplotlib.pyplot as plt


def f(x, t, D):
    sigma = np.sqrt(2*D*t)
    rho = 1./(np.sqrt(2*np.pi)*sigma**2)*np.exp(-x**2/(2*sigma**2))

    return rho



x_plot = np.linspace(-100, 100, 10001)
t_plot = np.linspace(1, 100, 100)

for i in range(len(t_plot)):
    if i%10 == 0:
        f(x_plot, t_plot[i], 2)


plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x_plot, f(x_plot, t_plot[0], 2), 'm-')  # Returns a tuple of line objects, thus the comma

for j in range(len(t_plot)):
    if j%1 == 0:
        line1.set_ydata(f(x_plot, t_plot[j], 2))
        fig.canvas.draw()
        fig.canvas.flush_events()

