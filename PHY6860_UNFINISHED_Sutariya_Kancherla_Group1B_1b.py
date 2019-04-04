import numpy as np
import math
import matplotlib.pyplot as plt
import random
from datetime import datetime

# Problem 1. b. Group Project
# Note: This part is unfinished (need to do overlay a Gaussian to the histogram and I
# believe this will involve some kind of fitting). The computing time for the N = 1 000 000
# array is really long, so if you just want to see the code run quickly, comment out the
# lines with "  ##" after them (lines: 44, 68-76)
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
array2 = gaussian_array(N2)  ##


# function for creating histograms with different number of bins
def hist_func(num_bins, N, array):
    plt.hist(array, num_bins, facecolor='blue')
    plt.title("Random Values = "+str(N))
    plt.xlabel("Bins = "+str(num_bins))
    plt.ylabel("Number of Random Values")

    # plot actual Gaussian on top of the histogram
    # UNFINISHED: We'll need to figure out how to do a fit to the histogram.

    # # This is simply plotting the given P(x), but that's way too small to show up on the hist.
    # xfit = []
    # yfit = []
    # xfit = np.linspace(-4, 4, 100)
    # yfit = f_max*2.7**(-xfit**2/2)  # used to be: f_max*math.exp(-xfit**2/2) but that resulted in an error
    # plt.plot(xfit, yfit)
    # plt.show()  Grant: in order to plot the gaussian curve on the same plot, need to show it later


def gaussian_plot(x, N):
    sigma = 1.0
    rho = N/(np.sqrt(2*np.pi)*sigma)*np.exp(-x**2/(2*sigma**2))

    plt.plot(x, rho, 'm--', label='Gaussian Fit')
    #plt.show()


x_gaussian = np.linspace(-10, 10, 1001)


# calling the histogram function for different bin values for N = 1000
hist_func(10, N1, array1)
gaussian_plot(x_gaussian, N1)
plt.show()

hist_func(20, N1, array1)   ##
gaussian_plot(x_gaussian, N1)
plt.show()

hist_func(50, N1, array1)   ##
gaussian_plot(x_gaussian, N1)
plt.show()

hist_func(100, N1, array1)  ##
gaussian_plot(x_gaussian, N1)
plt.show()


# calling the histogram function for different bin values for N = 1000000
hist_func(10, N2, array2)   ##
gaussian_plot(x_gaussian, N2)
plt.show()

hist_func(20, N2, array2)   ##
gaussian_plot(x_gaussian, N2)
plt.show()

hist_func(50, N2, array2)   ##
gaussian_plot(x_gaussian, N2)
plt.show()

hist_func(100, N2, array2)  ##
gaussian_plot(x_gaussian, N2)
plt.show()

