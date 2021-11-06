import matplotlib.pyplot as plt
import numpy as np
import csv
import robbyWorld
import robbyActions
import params


# Get strategy from Strategies library
def getStrategy():
    with open('Strategies/gaStrategy.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ')
        for row in csv_reader:
            myStrategy = row
        myStrategy = [int(float(i)) for i in myStrategy]
    return myStrategy


# Save a strategy as CSV in Strategies folder
def strategyToCSV():
    myStrategy = [4, 4, 6, 1, 2, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 0, 0, 6, 0, 0, 6,
              3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6,
              1, 1, 6, 1, 1, 6, 1, 1, 6, 2, 2, 6, 2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6,
              2, 2, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 3, 3, 6, 3, 3, 6, 3, 3, 6, 5, 5, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6,
              2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 0, 0, 6,
              0, 0, 6, 3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6,
              0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6,
              3, 3, 6, 2, 2, 6, 2, 2, 6, 4, 4, 6]

    with open('Strategies/gaStrategy.csv', 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=' ')
        my_writer.writerow(myStrategy)


# Copying totalScore function from robbyActions.py and breaking it to init() and animate(...) for UI
def init():
    board = np.add.outer(range(10), range(10, 0, -1)) % 2  # chessboard
    cans = robbyWorld.gencans()
    world = robbyWorld.genworld(cans)
    myStrategy = getStrategy()
    return board, cans, world, myStrategy


def animate(board, cans, world, myStrategy):
    x = 0
    y = 0
    total = 0

    for i in range(params.nofsteps):
        # Plotting 10x10 checkerboard
        fig = plt.figure(1)
        fig.suptitle(f"Robby's Score = {total}, Move #{i + 1}", fontsize=16)
        im1 = plt.imshow(board, cmap=plt.cm.tab20c, interpolation='nearest')
        # Overlaying cans over the board
        im2 = plt.imshow(cans, cmap=plt.cm.coolwarm, alpha=0.7, interpolation='nearest')
        north = world[x, y].north
        south = world[x, y].south
        west = world[x, y].west
        east = world[x, y].east
        current = world[x, y].current
        index = 3 ** 0 * current + 3 ** 1 * east + 3 ** 2 * west + 3 ** 3 * south + 3 ** 4 * north
        action = myStrategy[index]
        [x, y, score] = robbyActions.locationAndScore(world, x, y, action)
        total += score
        # Updating cans map in each run
        if action == 6:
            if cans[x, y] == 2:
                cans[x, y] = 0
        # Overlaying Robby's position
        robbyPosition = np.zeros((10, 10), int)
        robbyPosition[x, y] = 1
        im3 = plt.imshow(robbyPosition, cmap=plt.cm.Greys, alpha=0.5, interpolation='nearest')
        # Displaying plot
        plt.ion()
        plt.pause(1)
        plt.show()


board, cans, world, myStrategy = init()
animate(board, cans, world, myStrategy)
