import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import random
from datetime import datetime

# Problem 1. b. Group Project
# Note: The lines for N = 1 000 000 are commented out right now, to save on
# computing time while figuring out the histogram normalization
random.seed(datetime.now())

# setting the sizes of the two random value arrays
N1 = 1000
N2 = 1000000

# max value that the gaussian can have (y_max)
f_max = 1/math.sqrt(2*np.pi)


# function to get P(x)
def function(x):
    return f_max*math.exp(-x**2/2)


# making gaussian x value array using the Rejection (hit-or-miss) method
def gaussian_array(N):
    gauss_x = []  # initialize an empty array of values that are Gaussian-ly distributed
    i = 0
    while i < N:  # N is how many values the array of random values will have
        # Step 1: generate y value in [0, f_max]
        random_y = random.random()
        if random_y <= f_max:
            x_value = random.randint(-10, 10)  # generate x value in [-10, 10]
            if random_y <= function(x_value):  # compare random_y with f(x)
                gauss_x.append(x_value)
                i = i+1
    return gauss_x


# create gaussian arrays of two different sizes
array1 = gaussian_array(N1)
array2 = gaussian_array(N2)


# function for creating histograms with different number of bins
def hist_func(num_bins, N, array):
    # using np.hist to get the arrays that make up the histogram
    hist, bin_edges = np.histogram(array, num_bins, density=True)

    # normalizing the resulting histogram array
    hist_sum = hist.sum()
    hist_norm = hist / hist_sum

    # plotting the histogram using plt.bar
    bar_x_array = np.linspace(-4, 4, num_bins)
    plt.bar(bar_x_array, hist_norm, align='center')
    plt.title("Random Values = "+str(N))
    plt.xlabel("Bins = "+str(num_bins))
    plt.ylabel("Number of Random Values (normalized)")

    # plot actual Gaussian on top of the histogram
    xfit = []
    yfit = []
    xfit = np.linspace(-4, 4, 100)
    yfit = f_max*2.718**(-xfit**2/2)  # used to be: f_max*math.exp(-xfit**2/2)
    # but that resulted in an error (believe it was from math.exp)
    plt.plot(xfit, yfit,'--k')
    plt.show()


# calling the histogram function for different bin values for N = 1000
hist_func(10, N1, array1)
hist_func(20, N1, array1)
hist_func(50, N1, array1)
hist_func(100, N1, array1)

# calling the histogram function for different bin values for N = 1000000
hist_func(10, N2, array2)
hist_func(20, N2, array2)
hist_func(50, N2, array2)
hist_func(100, N2, array2)

