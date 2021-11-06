"""
Defines the environment that Robby operates in.
10 x 10 board with 20 cans randomly littered on the board.
Each square has the following attributes:
square.north = [0,1,2]  //0 - no can ; 1 - wall ; 2 - can
square.south = [0,1,2]  //0 - no can ; 1 - wall ; 2 - can
square.east = [0,1,2]  //0 - no can ; 1 - wall ; 2 - can
square.west = [0,1,2]  //0 - no can ; 1 - wall ; 2 - can
square.current = [0,1,2]  //0 - no can ; 1 - wall ; 2 - can
square.action = [0,1,2,3,4,5,6]  //see robbyActions for details on each action
"""

import numpy as np
import params


# A class to hold all relevant data for each square in robbyWorld
class Square:
    def __init__(self, x, y, north=0, south=0, east=0, west=0, current=0, action=0):
        self.x = x
        self.y = y
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.current = current
        self.action = action

    def checkcurrent(self, can):
        return can[self.x, self.y]

    def checknorth(self, can):
        if self.y == 0:
            wall = 1
            return wall
        else:
            return can[self.x, self.y - 1]

    def checksouth(self, can):
        if self.y == 9:
            wall = 1
            return wall
        else:
            return can[self.x, self.y + 1]

    def checkwest(self, can):
        if self.x == 0:
            wall = 1
            return wall
        else:
            return can[self.x - 1, self.y]

    def checkeast(self, can):
        if self.x == 9:
            wall = 1
            return wall
        else:
            return can[self.x + 1, self.y]

    def checkaction(self):
        action = np.random.randint(0, 7)
        return action


# Generate 20 cans randomly distributed in the array
def gencans():
    cans = np.zeros((params.xsize * params.ysize,), int)
    i = 0
    while i < params.nofcans:
        index = np.random.randint(0, 99)
        cans[index] = 2
        i = np.count_nonzero(cans)
    cans = cans.reshape(params.xsize, params.ysize)
    return cans


# Assigning values to all squares using class methods
def genworld(cans):
    worldMap = np.zeros((params.xsize, params.ysize), object)
    for x in range(params.xsize):
        for y in range(params.ysize):
            worldMap[x, y] = Square(x, y)
            worldMap[x, y].current = worldMap[x, y].checkcurrent(cans)
            worldMap[x, y].north = worldMap[x, y].checknorth(cans)
            worldMap[x, y].south = worldMap[x, y].checksouth(cans)
            worldMap[x, y].west = worldMap[x, y].checkwest(cans)
            worldMap[x, y].east = worldMap[x, y].checkeast(cans)
            worldMap[x, y].action = worldMap[x, y].checkaction()
    return worldMap
