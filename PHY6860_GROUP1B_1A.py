import matplotlib.pyplot as plt
import random
from datetime import datetime

# GROUP 1B: #1.a.
# setting a seed for the random function
random.seed(datetime.now())


# function for getting an array with N random values
def return_array(N):
    arr = []
    i = 0
    while i < N:
        arr.append(random.random())
        i = i+1
    return arr


# using the return_array function get arrays of two diff. sizes
N1 = 1000
N2 = 1000000
array1 = return_array(N1)
array2 = return_array(N2)


# function to create a histogram with varying bin size (10, 20, 50, 100)
def bin_plot(num_bins, bin_array, N):
    plt.hist(bin_array, num_bins, density=1, facecolor='blue')
    plt.title("Random Values = "+str(N))
    plt.xlabel("Bins = "+str(num_bins))
    plt.ylabel("Number of Random Values")
    plt.show()


# histograms for N = 1000
bin_plot(10, array1, N1)
bin_plot(20, array1, N1)
bin_plot(50, array1, N1)
bin_plot(100, array1, N1)

# histograms for N = 1,000,000
bin_plot(10, array2, N2)
bin_plot(20, array2, N2)
bin_plot(50, array2, N2)
bin_plot(100, array2, N2)

