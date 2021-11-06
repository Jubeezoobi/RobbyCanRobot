"""
Possible actions:
0 = move north
1 = move south
2 = move west
3 = move east
4 = move random
5 = stay put
6 = try to pick can

Possible strategies:
There are 3^5 = 243 actions that Robby can take
[North square, South square, East square, West square, Current square]
each can be either
[empty, can, wall]
An array of 243 cells each with a number between 0-6 (action) is a strategy for Robby to take

Scoring:
Picks a can = params.scoreCan
Tries to pick a can on empty square = params.scoreNoCan
Bumps into a wall = params.scoreWall
"""

import numpy as np
import params
import robbyWorld


# Calculating next [x, y] location of Robby based on his action
def locationAndScore(world, x, y, action):
    score = 0
    if action == 0:  # Move north
        if y > 0:
            y -= 1
        else:
            score += params.scoreWall  # Crashes into north wall
    elif action == 1:  # Move south
        if y < params.ysize - 1:
            y += 1
        else:
            score += params.scoreWall  # Crashes into south wall
    elif action == 2:  # Move west
        if x > 0:
            x -= 1
        else:
            score += params.scoreWall  # Crashes into west wall
    elif action == 3:  # Move east
        if x < params.xsize - 1:
            x += 1
        else:
            score += params.scoreWall  # Crashes into east wall
    elif action == 4:  # Move random
        action = np.random.randint(0, 4)
        locationAndScore(world, x, y, action)
    elif action == 5:  # Stay put
        pass
    elif action == 6:  # Pick up can
        if world[x, y].current == 2:
            world[x, y].current = 0
            score += params.scoreCan  # Picks a can
        elif world[x, y].current == 0:
            score += params.scoreNoCan  # Tries to pick up can where there's no can
    else:
        print("Error: Robby's action is out of range")
    return x, y, score


# Converting 'world' data to strategy
# North     South   West    East    Current
#   0         0       0       0       0
#   0         0       0       0       1
# And so on...


# Working through nofsteps of Robby
def totalScore(world, strategy):
    x = 0
    y = 0
    total = 0

    for i in range(params.nofsteps):
        north = world[x, y].north
        south = world[x, y].south
        west = world[x, y].west
        east = world[x, y].east
        current = world[x, y].current
        index = 3 ** 0 * current + 3 ** 1 * east + 3 ** 2 * west + 3 ** 3 * south + 3 ** 4 * north
        action = strategy[index]
        [x, y, score] = locationAndScore(world, x, y, action)
        total += score
    return total


# Run strategy params.nrep times on different cans configurations (different 'worlds')
# and calculate average score

def scoreavg(strategy):
    scoreSum = 0
    for i in range(params.nrep):
        cans = robbyWorld.gencans()
        world = robbyWorld.genworld(cans)
        score = totalScore(world, strategy)
        scoreSum += score
    scoreAvg = scoreSum / params.nrep
    return scoreAvg
