import numpy as np
import matplotlib.pyplot as plt



def predator_prey(N=10, N_t=100, fish_0=1, shark_0=0, fish_reproduce=7, shark_reproduce=7, starve=3):
    # setup lattice
    gridx = np.linspace(-(N-1)/2, (N-1)/2)
    gridy = np.linspace(-(N-1)/2, (N-1)/2)
    x, y = np.meshgrid(gridx, gridy)


    shark = -1*np.ones((N, N))
    fish = -1*np.ones((N, N))
    shark_ate = np.zeros((N, N))

    count_fish = [fish_0]
    count_shark = [shark_0]

    num_fish = 0
    num_shark = 0



    while num_fish < fish_0:
        x_tmp = np.random.randint(0, N)
        y_tmp = np.random.randint(0, N)
        if fish[x_tmp, y_tmp] == -1:
            fish[x_tmp, y_tmp] = 0
            num_fish += 1

    while num_shark < shark_0:
        x_tmp = np.random.randint(0, N)
        y_tmp = np.random.randint(0, N)
        if shark[x_tmp, y_tmp] == -1:
            shark[x_tmp, y_tmp] = 0
            num_shark += 1



    t = np.linspace(0, N_t, N_t+1)
    for p in range(N_t):
        shark_move = np.zeros((N, N))  # set all fish and sharks to "unmoved" at the start of each time step
        fish_move = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                if fish[i, j] != -1 and fish_move[i, j] == 0:  # if a fish is at (i,j) that hasn't been moved this time step
                    fish_neighbors = []
                    if i == 0 and j == 0:
                        fish_neighbors_tmp = [(N-1, j), (i, N-1), (i+1, j), (i, j+1)]
                    elif i == 0 and j == N-1:
                        fish_neighbors_tmp = [(N-1, j), (i, j-1), (i+1, j), (i, 0)]
                    elif i == N-1 and j == 0:
                        fish_neighbors_tmp = [(i-1, j), (i, N-1), (0, j), (i, j+1)]
                    elif i == N-1 and j == N-1:
                        fish_neighbors_tmp = [(i-1, j), (i, j-1), (0, j), (i, 0)]
                    elif i == 0:
                        fish_neighbors_tmp = [(N-1, j), (i, j-1), (i+1, j), (i, j+1)]
                    elif i == N-1:
                        fish_neighbors_tmp = [(i-1, j), (i, j-1), (0, j), (i, j+1)]
                    elif j == 0:
                        fish_neighbors_tmp = [(i-1, j), (i, N-1), (i+1, j), (i, j+1)]
                    elif j == N-1:
                        fish_neighbors_tmp = [(i-1, j), (i, j-1), (i+1, j), (i, 0)]
                    else:
                        fish_neighbors_tmp = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]


                    for f in fish_neighbors_tmp:
                        if fish[f] == -1 and shark[f] == -1:
                            fish_neighbors.append(f)

                    if len(fish_neighbors) != 0:
                        rand = np.random.randint(0, len(fish_neighbors))  # choose where the fish swims to next
                        fish_move[fish_neighbors[rand]] = 1

                        if fish[i, j] >= fish_reproduce:
                            fish[fish_neighbors[rand]] = 0  # both new and old fish return to 0 age
                            fish[i, j] = 0
                            fish_move[i, j] = 1
                        else:
                            fish[fish_neighbors[rand]] = fish[i, j] + 1
                            fish[i, j] = -1
                            fish_move[i, j] = 1
                    else:
                        fish[i, j] += 1
                        fish_move[i, j] = 1


        count_fish_tmp = 0
        for a in range(N):
            for b in range(N):
                if fish[a, b] != -1:
                    count_fish_tmp += 1

        count_fish.append(count_fish_tmp)
        print(count_fish_tmp)

    return fish, count_fish, t


results = predator_prey()

test_fish = results[1]
test_time = results[2]


plt.plot(test_time, test_fish, 'm')
plt.show()

