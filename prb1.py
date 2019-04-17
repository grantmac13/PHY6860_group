import numpy as np
import matplotlib.pyplot as plt


grid = []
span = []
pct = []
prb = []
critical = []
for N in [5, 10, 15, 20, 30, 50, 80]:
    pct.clear()
    span.clear()
    prb.clear()
    for P in range(100):
        spanpct = 0
        for A in range(100):
            lat = np.zeros((N, N))
            clus = np.zeros((N, N))
            for i in range(N):
                for j in range(N):
                    lat[i, j] = np.random.randint(1, 101)
                    if lat[i, j] < P:
                        lat[i, j] = 1
                    else:
                        lat[i, j] = 0
            for i in range(N):
                for j in range(N):
                    if i == 0 and j != 0 and j != N - 1:
                        if lat[i, j] == 1:
                            if lat[i + 1, j] and lat[i, j + 1] and lat[i, j - 1] != 1:
                                clus[i, j] = 1
                        if clus[i + 1, j] or clus[i, j + 1] or clus[i, j - 1] == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i, j] == 1 and clus[i, j] != a - 1 and (
                                    lat[i + 1, j], lat[i, j + 1], lat[i, j - 1]) != 1:
                                clus[i, j] = a
                            if clus[i + 1, j] or clus[i, j + 1] or clus[i, j - 1] == a:
                                clus[i, j] = a
                    if i == N - 1 and j != 0 and j != N - 1:
                        if lat[i, j] == 1 and (lat[i - 1, j], lat[i, j + 1], lat[i, j - 1]) != 1:
                            clus[i, j] = 1
                        if (clus[i - 1, j], clus[i, j + 1], clus[i, j - 1]) == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i, j] == 1 and clus[i, j] != a - 1 and (
                                    lat[i - 1, j], lat[i, j + 1], lat[i, j - 1]) != 1:
                                clus[i, j] = a
                            if clus[i - 1, j] or clus[i, j + 1] or clus[i, j - 1] == a:
                                clus[i, j] = a
                    if j == 0 and i != 0 and i != N - 1:
                        if lat[i, j] == 1 and (lat[i + 1, j], lat[i - 1, j], lat[i, j + 1]) != 1:
                            clus[i, j] = 1
                        elif (clus[i + 1, j], clus[i - 1, j], clus[i, j + 1]) == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i, j] == 1 and clus[i, j] != a - 1 and (
                                    lat[i + 1, j], lat[i - 1, j], lat[i, j + 1]) != 1:
                                clus[i, j] = a
                            if clus[i + 1, j] or clus[i - 1, j] or clus[i, j + 1] == a:
                                clus[i, j] = a
                    if j == N - 1 and i != 0 and i != N - 1:
                        if lat[i, j] == 1 and (lat[i + 1, j], lat[i - 1, j], lat[i, j - 1]) != 1:
                            clus[i, j] = 1
                        elif (clus[i + 1, j], clus[i - 1, j], clus[i, j - 1]) == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i, j] == 1 and clus[i, j] != a - 1 and (
                                    lat[i + 1, j], lat[i - 1, j], lat[i, j - 1]) != 1:
                                clus[i, j] = a
                            if clus[i + 1, j] or clus[i - 1, j] or clus[i, j - 1] == a:
                                clus[i, j] = a
                    if i == 0 and j == 0:
                        if lat[i, j] == 1 and (lat[i + 1, j], lat[i, j + 1],) != 1:
                            clus[i, j] = 1
                        if (clus[i + 1, j], clus[i, j + 1]) == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i, j] == 1 and clus[i, j] != a - 1 and (lat[i + 1, j], lat[i, j + 1]) != 1:
                                clus[i, j] = a
                            if clus[i + 1, j] or clus[i, j + 1] == a:
                                clus[i, j] = a
                    if i == 0 and j == N - 1:
                        if lat[i, j] == 1 and (lat[i + 1, j], lat[i, j - 1]) != 1:
                            clus[i, j] = 1
                        if (clus[i + 1, j], clus[i, j - 1]) == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i, j] == 1 and clus[i, j] != a - 1 and (lat[i + 1, j], lat[i, j - 1]) != 1:
                                clus[i, j] = a
                            if clus[i + 1, j] or clus[i, j - 1] == a:
                                clus[i, j] = a
                    if i == N - 1 and j == 0:
                        if lat[i, j] == 1 and (lat[i - 1, j], lat[i, j + 1]) != 1:
                            clus[i, j] = 1
                        if (clus[i - 1, j], clus[i, j + 1]) == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i, j] == 1 and clus[i, j] != a - 1 and (lat[i - 1, j], lat[i, j + 1]) != 1:
                                clus[i, j] = a
                            if clus[i - 1, j] or clus[i, j + 1] == a:
                                clus[i, j] = a
                    if i == N - 1 and j == N - 1:
                        if lat[i, j] == 1 and (lat[i - 1, j], lat[i, j - 1]) != 1:
                            clus[i, j] = 1
                        if (clus[i - 1, j], clus[i, j - 1]) == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i, j] == 1 and clus[i, j] != a - 1 and (lat[i - 1, j], lat[i, j - 1]) != 1:
                                clus[i, j] = a
                            if clus[i - 1, j] or clus[i, j - 1] == a:
                                clus[i, j] = a
                    if i != 0 and i != N - 1 and j != 0 and j != N - 1:
                        if lat[i, j] == 1 and (lat[i + 1, j], lat[i - 1, j], lat[i, j + 1], lat[i, j - 1]) != 1:
                            clus[i, j] = 1
                        if (clus[i + 1, j], clus[i - 1, j], clus[i, j + 1], clus[i, j - 1]) == 1:
                            clus[i, j] = 1
                        for a in range(2, int((N**2)/6)):
                            if lat[i,j] == 1 and clus[i,j] != a-1 and (lat[i+1,j], lat[i-1,j], lat[i,j+1], lat[i,j-1]) != 1:
                                clus[i, j] = a
                            if clus[i + 1, j] or clus[i - 1, j] or clus[i, j + 1] or clus[i, j - 1] == a:
                                clus[i, j] = a
            cluster = 0
            for i in range(N):
                for j in range(N):
                    for a in range(N):
                        if clus[i, 0] == clus[a, N - 1] and clus[i, 0] != 0:
                            cluster = 1
                        if clus[0, j] == clus[N - 1, a] and clus[0, j] != 0:
                            cluster = 1
            if cluster == 1:
                spanpct += 1
        prb.append(P)
        span.append(spanpct)
        if spanpct == 98:
            pct.append(P)
    critical.append(pct[0])
    grid.append(N)
    print(N)
    plt.plot(span, prb, 'b', label="Percolation on grid with dimension length " + str(N))
    plt.legend()
plt.show()
plt.plot(grid, critical)
