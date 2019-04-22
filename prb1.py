import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

grid = []  # defining arrays for graphs
pct = []
critical = []

for N in [5, 10, 15, 20, 30, 50, 80]:   # grid sizes
    pct.clear()
    span = np.zeros((N, N))
    spanct = 0
    for P in range(100):   # probability of each point on lattice being filled
        lat = np.zeros((N, N))
        clus = np.zeros((N, N))
        c = 0
        for i in range(N):
            for j in range(N):
                lat[i, j] = np.random.randint(1, 101)   # random simulator to generate a lattice
                if lat[i, j] < P:
                    lat[i, j] = 1
                else:
                    lat[i, j] = 0
        for i in range(N):
            for j in range(N):  # loop to test whether each lattice has a spanning cluster
                if lat[i, j] == 0:
                    clus[i, j] = 0
                elif i == 0 and j != 0 and j != N - 1:
                    if lat[i, j] == 1 and (lat[i + 1, j] and lat[i, j + 1] and lat[i, j - 1] == 0):
                        c += 1
                        clus[i, j] = c
                    if clus[i, j-1] != 0:
                        clus[i, j] = clus[i, j-1]
                elif i == N - 1 and j != 0 and j != N - 1:
                    if lat[i, j] == 1 and (lat[i - 1, j] and lat[i, j + 1] and lat[i, j - 1] == 0):
                        c += 1
                        clus[i, j] = c
                    if clus[i - 1, j] != 0:
                        clus[i, j] = clus[i-1, j]
                    if clus[i, j-1] != 0:
                        clus[i, j] = clus[i, j-1]
                elif j == 0 and i != 0 and i != N - 1:
                    if lat[i, j] == 1 and (lat[i + 1, j] and lat[i - 1, j] and lat[i, j + 1] == 0):
                        c += 1
                        clus[i, j] = c
                    if clus[i - 1, j] != 0:
                        clus[i, j] = clus[i-1, j]
                elif j == N - 1 and i != 0 and i != N - 1:
                    if lat[i, j] == 1 and (lat[i + 1, j] and lat[i - 1, j] and lat[i, j - 1] == 0):
                        c += 1
                        clus[i, j] = c
                    if clus[i - 1, j] != 0:
                        clus[i, j] = clus[i-1, j]
                    if clus[i, j-1] != 0:
                        clus[i, j] = clus[i, j-1]
                elif i == 0 and j == 0:
                    if lat[i, j] == 1:
                        clus[i, j] = 1
                elif i == 0 and j == N - 1:
                    if lat[i, j] == 1 and (lat[i + 1, j] and lat[i, j - 1] == 0):
                        c += 1
                        clus[i, j] = c
                    if clus[i, j-1] != 0:
                        clus[i, j] = clus[i, j-1]
                elif i == N - 1 and j == 0:
                    if lat[i, j] == 1 and (lat[i - 1, j] and lat[i, j + 1] == 0):
                        c += 1
                        clus[i, j] = c
                    if clus[i - 1, j] != 0:
                        clus[i, j] = clus[i-1, j]
                elif i == N - 1 and j == N - 1:
                    if lat[i, j] == 1 and (lat[i - 1, j] and lat[i, j - 1] == 0):
                        c += 1
                        clus[i, j] = c
                    if clus[i - 1, j] != 0:
                        clus[i, j] = clus[i-1, j]
                    if clus[i, j-1] != 0:
                        clus[i, j] = clus[i, j-1]
                elif i != 0 and i != N-1 and j != 0 and j != N-1:
                    if lat[i, j] == 1 and (lat[i + 1, j] and lat[i - 1, j] and lat[i, j + 1] and lat[i, j - 1] == 0):
                        c += 1
                        clus[i, j] = c
                    if clus[i - 1, j] != 0:
                        clus[i, j] = clus[i-1, j]
                    if clus[i, j-1] != 0:
                        clus[i, j] = clus[i, j-1]
                else:
                    clus[i, j] = 1

        cluster = 0
        for x in range(50):    # combines clusters which start separate but intersect
            for i in range(N):
                for j in range(N):
                    for a in range(1, N):
                        if i == 0 and j != 0 and j != N - 1:
                            if clus[i, j] == a and 0 < clus[i + 1, j] < a:
                                clus[i, j] = clus[i + 1, j]
                            elif clus[i, j] == a and 0 < clus[i, j + 1] < a:
                                clus[i, j] = clus[i, j + 1]
                            elif clus[i, j] == a and 0 < clus[i, j - 1] < a:
                                clus[i, j] = clus[i, j - 1]
                        elif i == N - 1 and j != 0 and j != N - 1:
                            if clus[i, j] == a and 0 < clus[i, j + 1] < a:
                                clus[i, j] = clus[i, j + 1]
                            elif clus[i, j] == a and 0 < clus[i, j - 1] < a:
                                clus[i, j] = clus[i, j - 1]
                            elif clus[i, j] == a and 0 < clus[i-1, j] < a:
                                clus[i, j] = clus[i-1, j]
                        elif j == 0 and i != 0 and i != N - 1:
                            if clus[i, j] == a and 0 < clus[i + 1, j] < a:
                                clus[i, j] = clus[i + 1, j]
                            elif clus[i, j] == a and 0 < clus[i, j + 1] < a:
                                clus[i, j] = clus[i, j + 1]
                            elif clus[i, j] == a and 0 < clus[i-1, j] < a:
                                clus[i, j] = clus[i-1, j]
                        elif j == N - 1 and i != 0 and i != N - 1:
                            if clus[i, j] == a and 0 < clus[i + 1, j] < a:
                                clus[i, j] = clus[i + 1, j]
                            elif clus[i, j] == a and 0 < clus[i, j - 1] < a:
                                clus[i, j] = clus[i, j - 1]
                            elif clus[i, j] == a and 0 < clus[i-1, j] < a:
                                clus[i, j] = clus[i-1, j]
                        elif i == 0 and j == 0:
                            if clus[i, j] == a and 0 < clus[i + 1, j] < a:
                                clus[i, j] = clus[i + 1, j]
                            elif clus[i, j] == a and 0 < clus[i, j + 1] < a:
                                clus[i, j] = clus[i, j + 1]
                        elif i == 0 and j == N - 1:
                            if clus[i, j] == a and 0 < clus[i + 1, j] < a:
                                clus[i, j] = clus[i + 1, j]
                            elif clus[i, j] == a and 0 < clus[i, j - 1] < a:
                                clus[i, j] = clus[i, j - 1]
                        elif i == N - 1 and j == 0:
                            if clus[i, j] == a and 0 < clus[i, j + 1] < a:
                                clus[i, j] = clus[i, j + 1]
                            elif clus[i, j] == a and 0 < clus[i-1, j] < a:
                                clus[i, j] = clus[i-1, j]
                        elif i == N - 1 and j == N - 1:
                            if clus[i, j] == a and 0 < clus[i, j - 1] < a:
                                clus[i, j] = clus[i, j - 1]
                            elif clus[i, j] == a and 0 < clus[i-1, j] < a:
                                clus[i, j] = clus[i-1, j]
                        elif i != 0 and i != N - 1 and j != 0 and j != N - 1:
                            if clus[i, j] == a and 0 < clus[i + 1, j] < a:
                                clus[i, j] = clus[i + 1, j]
                            elif clus[i, j] == a and 0 < clus[i, j + 1] < a:
                                clus[i, j] = clus[i, j + 1]
                            elif clus[i, j] == a and 0 < clus[i, j - 1] < a:
                                clus[i, j] = clus[i, j - 1]
                            elif clus[i, j] == a and 0 < clus[i-1, j] < a:
                                clus[i, j] = clus[i-1, j]

        for i in range(N):  # defines spanning cluster
            for j in range(N):
                for a in range(N):
                    if clus[i, 0] == clus[a, N - 1] and clus[i, 0] != 0:
                        cluster = 1
                    if clus[0, j] == clus[N - 1, a] and clus[0, j] != 0:
                        cluster = 1
        if cluster == 1:  # counting spanning clusters
            spanct += 1
            pct.append(P)
        if cluster == 1 and spanct == 3:  # minimize error effects
                span = lat

    # create discrete colormap
    cmap = colors.ListedColormap(['red', 'blue'])
    bounds = [-.5, .5, 1.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots()

    ax.imshow(span, cmap=cmap, norm=norm)
    plt.title("First spanning cluster for " + str(N) + " X " + str(N) + " grid (cluster in blue)")
    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, N+.5, 1));
    ax.set_yticks(np.arange(-.5, N+.5, 1));
    critical.append(pct[2])
    grid.append(N)


plt.show()
plt.plot(grid, critical, 'b*')
plt.plot(grid, critical, 'g-')
plt.xlim(85, 0)
plt.title("2D percolation with varying dimension length")
plt.xlabel("dimension length")
plt.ylabel("critical percentage")
plt.show()

