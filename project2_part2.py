import numpy as np
import matplotlib.pyplot as plt


# dummy lattice size 10x10
# N = 10
# M = 10

# arbitrary number of time steps 10000
# N_t = 10000

# arbitrary initial number of fish=10 and sharks=5
# fish_0 = 10
# shark_0 = 5


# number of timesteps to reproduce
# fish_reproduce = 5
# shark_reproduce = 6

# number of timesteps to starve to death
# starve = 7


def predator_prey(N=100, M=100, N_t=100, fish_0=0, shark_0=100, fish_reproduce=5, shark_reproduce=10, starve=3):
    # setup lattice
    gridx = np.linspace(-(N-1)/2, (N-1)/2)
    gridy = np.linspace(-(M-1)/2, (M-1)/2)
    x, y = np.meshgrid(gridx, gridy)


    shark = -1*np.ones((N, M))
    fish = -1*np.ones((N, M))


    shark_ate = np.zeros((N, M))

    count_fish = [fish_0]
    count_shark = [shark_0]

    for l in range(fish_0):
        x_tmp = np.random.randint(0, N-1)
        y_tmp = np.random.randint(0, M-1)

        fish[x_tmp, y_tmp] = 0

    for l in range(shark_0):
        x_tmp = np.random.randint(0, N-1)
        y_tmp = np.random.randint(0, M-1)

        shark[x_tmp, y_tmp] = 0

    t = np.linspace(0, N_t-1, N_t)
    for p in range(N_t-1):
        for i in range(N-1):
            for j in range(M-1):

                if fish[i, j] != -1:  # if a fish is at (i,j)
                    fish_neighbors = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]  # set list of neighbor sites for each fish

                    ### ATTEMPTED PERIODIC BOUNDARY CONDITIONS
                    if i == 0:
                        if j == 0:
                            fish_neighbors = [(N - 1, j), (i, M - 1), (i + 1, j), (i, j + 1)]
                        if j == M - 1:
                            fish_neighbors = [(N - 1, j), (i, j - 1), (i + 1, j), (i, 0)]
                    if i == N-1:
                        if j == 0:
                            fish_neighbors = [(i-1, j), (i, M-1), (0, j), (i, j+1)]
                        if j == M-1:
                            fish_neighbors = [(i-1, j), (i, j-1), (0, j), (i, 0)]
                    else:
                        fish_neighbors = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]

                    rand = np.random.randint(0, 3)  # choose where the fish swims to next
                    fish[fish_neighbors[rand]] = fish[i, j] + 1

                    if fish[i, j] == fish_reproduce:  # check fish reproduction criterion
                        fish[i, j] = 0
                    else:
                        fish[i, j] = -1

                if shark[i, j] != -1:
                    adjacent_fish = []
                    shark_neighbors = []
                    ### ATTEMPTED PERIODIC BOUNDARY CONDITIONS
                    if i == N-1:
                        if j == 0:
                            shark_neighbors = [(i-1, j), (i, M-1), (0, j), (i, j+1)]
                        if j == M-1:
                            shark_neighbors = [(i-1, j), (i, j-1), (0, j), (i, 0)]
                    elif i == 0:
                        if j == 0:
                            shark_neighbors = [(N-1, j), (i, M-1), (i+1, j), (i, j+1)]
                        if j == M-1:
                            shark_neighbors = [(N-1, j), (i, j-1), (i+1, j), (i, 0)]
                    else:
                        shark_neighbors = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]

                    for k in range(len(shark_neighbors)-1):
                        if fish[shark_neighbors[k]] != -1:  # find number of neighbor sites with fish
                            adjacent_fish.append(k)

                    if len(adjacent_fish) > 1:  # if more than one fish is nearby
                        rand = np.random.randint(0, len(adjacent_fish)-1)  # choose a neighbor site at random
                        shark[shark_neighbors[rand]] = shark[i, j] + 1  # age shark by 1
                        shark_ate[shark_neighbors[rand]] = p  # update array for when shark last ate

                        if shark[i, j] == shark_reproduce:  # check reproduction criterion
                            shark[i, j] = 0
                            shark_ate[i, j] = p  # new fish "last ate" when they first appear

                        else:
                            shark[i, j] = -1

                    elif len(adjacent_fish) == 1:  # if only one fish is nearby, go eat it
                        shark[adjacent_fish[0]] = shark[i, j] + 1  # age shark by 1

                        if shark[i, j] == shark_reproduce:  # check reproduction criterion
                            shark[i, j] = 0

                        else:
                            shark[i, j] = -1

                    else:
                        shark_neighbors = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]  # choose random neighbor
                        rand = np.random.randint(0, 3)
                        shark[shark_neighbors[rand]] = shark[i, j] + 1  # age shark by 1

                        if shark[i, j] == shark_reproduce:  # check reproduction criterion
                            shark[i, j] = 0
                        else:
                            shark[i, j] = -1


                    if shark_ate[i, j] == p-starve:  # check if shark has starved
                        shark[i, j] = -1

        count_fish_tmp = 0
        count_shark_tmp = 0
        for a in range(N-1):
            for b in range(M-1):
                if fish[a, b] != -1:
                    count_fish_tmp += 1
                if shark[a, b] != -1:
                    count_shark_tmp += 1

        count_fish.append(count_fish_tmp)
        count_shark.append(count_shark_tmp)

    return fish, shark, count_fish, count_shark, shark_ate, t


results = predator_prey()

test_fish = results[2]
test_shark = results[3]
test_time = results[5]




plt.plot(test_time, test_fish, 'r')
plt.plot(test_time, test_shark, 'g')
plt.show()

