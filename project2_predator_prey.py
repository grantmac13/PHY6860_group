import numpy as np
import matplotlib.pyplot as plt



def predator_prey(fish_0, shark_0, fish_reproduce, shark_reproduce, starve, N_t=300, N=10):
    # setup lattice

    gridx = np.linspace(-N/2, N/2)
    gridy = np.linspace(-N/2, N/2)
    x, y = np.meshgrid(gridx, gridy)

    if shark_0 + fish_0 > N**2:
        shark_0 = N**2 - fish_0


    shark = -1*np.ones((N, N))
    fish = -1*np.ones((N, N))
    shark_ate = np.zeros((N, N))


    count_fish = [fish_0]
    count_shark = [shark_0]

    list_fish = []
    list_shark = []

    num_fish = 0
    num_shark = 0

    ## while loop just in case an occupied site is chosen when placing initial fish
    while num_fish < fish_0:
        x_tmp = np.random.randint(0, N)
        y_tmp = np.random.randint(0, N)
        if fish[x_tmp, y_tmp] == -1:
            fish[x_tmp, y_tmp] = 0
            num_fish += 1

    ## while loop just in case an occupied site is chosen when placing initial sharks
    while num_shark < shark_0:
        x_tmp = np.random.randint(0, N)
        y_tmp = np.random.randint(0, N)
        if shark[x_tmp, y_tmp] == -1 and fish[x_tmp, y_tmp] == -1:
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


                ### STARTING SHARK CODE
                if shark[i, j] != -1 and shark_move[i, j] == 0:  # if a fish is at (i,j) that hasn't been moved this time step
                    shark_neighbors = []
                    adjacent_fish = []
                    if i == 0 and j == 0:
                        shark_neighbors_tmp = [(N-1, j), (i, N-1), (i+1, j), (i, j+1)]
                    elif i == 0 and j == N-1:
                        shark_neighbors_tmp = [(N-1, j), (i, j-1), (i+1, j), (i, 0)]
                    elif i == N-1 and j == 0:
                        shark_neighbors_tmp = [(i-1, j), (i, N-1), (0, j), (i, j+1)]
                    elif i == N-1 and j == N-1:
                        shark_neighbors_tmp = [(i-1, j), (i, j-1), (0, j), (i, 0)]
                    elif i == 0:
                        shark_neighbors_tmp = [(N-1, j), (i, j-1), (i+1, j), (i, j+1)]
                    elif i == N-1:
                        shark_neighbors_tmp = [(i-1, j), (i, j-1), (0, j), (i, j+1)]
                    elif j == 0:
                        shark_neighbors_tmp = [(i-1, j), (i, N-1), (i+1, j), (i, j+1)]
                    elif j == N-1:
                        shark_neighbors_tmp = [(i-1, j), (i, j-1), (i+1, j), (i, 0)]
                    else:
                        shark_neighbors_tmp = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]


                    for f in shark_neighbors_tmp:
                        if shark[f] == -1 and fish[f] == -1:
                            shark_neighbors.append(f)
                        if shark[f] == -1 and fish[f] != -1:
                            adjacent_fish.append(f)

                    if len(adjacent_fish) != 0:
                        rand = np.random.randint(0, len(adjacent_fish))  # choose where the fish swims to next
                        shark_move[adjacent_fish[rand]] = 1
                        shark_ate[adjacent_fish[rand]] = p
                        fish[adjacent_fish[rand]] = -1
                        shark_move[i, j] = 1

                        if shark[i, j] >= shark_reproduce:
                            shark[adjacent_fish[rand]] = 0  # both new and old fish return to 0 age
                            shark[i, j] = 0
                            shark_ate[i, j] = p  # new fish "ate" when it was "born"
                        else:
                            shark[adjacent_fish[rand]] = shark[i, j] + 1
                            shark[i, j] = -1

                    elif len(shark_neighbors) != 0:
                        rand = np.random.randint(0, len(shark_neighbors))  # choose where the fish swims to next
                        shark_move[shark_neighbors[rand]] = 1

                        if shark[i, j] >= shark_reproduce:
                            shark[shark_neighbors[rand]] = 0  # both new and old fish return to 0 age
                            shark[i, j] = 0
                            shark_ate[i, j] = p
                            shark_move[i, j] = 1
                        else:
                            shark[shark_neighbors[rand]] = shark[i, j] + 1
                            shark[i, j] = -1
                            shark_move[i, j] = 1

                        if shark_ate[shark_neighbors[rand]] <= p - starve:
                            shark[shark_neighbors[rand]] = -1  # not totally sure where to kill the starved sharks...


                    else:
                        shark[i, j] += 1
                        shark_move[i, j] = 1

                        if shark_ate[i, j] <= p - starve:
                            shark[i, j] = -1  # not totally sure where to kill the starved sharks...


        count_fish_tmp = 0
        count_shark_tmp = 0
        for a in range(N):
            for b in range(N):
                if fish[a, b] != -1:
                    count_fish_tmp += 1
                if shark[a, b] != -1:
                    count_shark_tmp += 1

        count_fish.append(count_fish_tmp)
        count_shark.append(count_shark_tmp)

        list_fish.append(fish)
        list_shark.append(shark)


        if (p-1)%(N_t/10) == 0:
            tmp_fish = fish + np.ones_like(fish)
            tmp_shark = shark + np.ones_like(shark)

            plt.scatter(x, y, tmp_fish, 'm')
            plt.scatter(x, y, tmp_shark, 'g')
            plt.ylabel("x")
            plt.xlabel("y")
            plt.title("Snapshot for step #"+str(p)+" of the numerical simulation")
            plt.savefig("fish_shark_step"+str(p)+".png")

            plt.show()

    return list_fish, list_shark, count_fish, count_shark, t


results = predator_prey(30, 5, 2, 8, 3)

test_fish = results[2]
test_shark = results[3]
test_time = results[-1]



plt.plot(test_time, test_shark, 'g', label="Shark Population")
plt.plot(test_time, test_fish, 'm', label="Fish Population")
plt.ylabel("Population")
plt.xlabel("Time")
plt.title("Attempting to achieve an equilibrium")
plt.show()


