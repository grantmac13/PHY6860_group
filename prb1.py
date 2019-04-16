from numpy import *
import matplotlib.pyplot as plt

N = 1  # temp
P = 50  # temp
lat = zeros[(N, N)]
clus = zeros[(N, N)]
for i in range(N):
    for j in range(N):
        lat[i, j] = random.randint(1, 101)
        if lat[i, j] > P:
            lat[i, j] = 1
        else:
            lat[i, j] = 0
for i in range(N):
    for j in range(N):
        if lat[i, j] == 1 and (lat[i+1, j], lat[i-1, j], lat[i, j+1], lat[i, j-1]) != 1:
            clus[i, j] == 1
        elif (clus[i+1, j], clus[i-1, j], clus[i, j+1], clus[i, j-1]) == 1:
            clus[i, j] == 1
        for a in range(2, 10):
            if lat[i, j] == 1 and clus[i, j] != a-1 and (lat[i + 1, j], lat[i - 1, j], lat[i, j + 1], lat[i, j - 1]) != 1:
                clus[i, j] == a
            if (clus[i + 1, j], clus[i - 1, j], clus[i, j + 1], clus[i, j - 1]) == 2:
                clus[i, j] == a
cluster = 0
for i in range(N):
    for j in range(N):
        for a in range((-N+1),N):
            if clus[i, 0] == clus[i+a, N-1]:
                cluster = 1
            if clus[0, j] == clus[N-1, j+a]:
                cluster = 1

