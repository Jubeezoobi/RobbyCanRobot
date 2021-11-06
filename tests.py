# Testing and debug
import numpy as np
import params
import robbyWorld
import robbyActions
import crossover


# ==========   robbyWorld Tests   ==========

# Testing gencans() function for creating 10x10 array with 20 cans
def testCans():
    cans = robbyWorld.gencans()
    assert np.shape(cans)[0] == params.xsize
    assert np.shape(cans)[1] == params.ysize
    assert np.count_nonzero(cans) == params.nofcans
    assert np.sum(cans) == 2 * params.nofcans


# Testing genworld(cans) function for creating 10x10 world and verifying the corners and center squares
def testWorldCorners():
    cans = robbyWorld.gencans()
    world = robbyWorld.genworld(cans)
    assert np.shape(world)[0] == params.xsize
    assert np.shape(world)[1] == params.ysize

    assert world[0, 0].north == 1
    assert world[0, 0].south != 1
    assert world[0, 0].west == 1
    assert world[0, 0].east != 1

    assert world[params.xsize - 1, 0].north == 1
    assert world[params.xsize - 1, 0].south != 1
    assert world[params.xsize - 1, 0].west != 1
    assert world[params.xsize - 1, 0].east == 1

    assert world[0, params.ysize - 1].north != 1
    assert world[0, params.ysize - 1].south == 1
    assert world[0, params.ysize - 1].west == 1
    assert world[0, params.ysize - 1].east != 1

    assert world[params.xsize - 1, params.ysize - 1].north != 1
    assert world[params.xsize - 1, params.ysize - 1].south == 1
    assert world[params.xsize - 1, params.ysize - 1].west != 1
    assert world[params.xsize - 1, params.ysize - 1].east == 1

    assert world[params.xsize - 5, params.ysize - 5].north != 1
    assert world[params.xsize - 5, params.ysize - 5].south != 1
    assert world[params.xsize - 5, params.ysize - 5].west != 1
    assert world[params.xsize - 5, params.ysize - 5].east != 1


# Testing genworld(cans) function for creating world with 20 cans
def testWorldCans():
    cans = robbyWorld.gencans()
    world = robbyWorld.genworld(cans)
    sumCans = 0
    for i in range(params.xsize):
        for j in range(params.ysize):
            if world[i, j].current == 2:
                sumCans += 2
    assert sumCans == 2 * params.nofcans


# ==========   robbyActions Tests   ==========

# Testing locationAndScore(world, x, y, action) function for choosing the correct action in myStrategy
def testAction():
    for i in range(params.nrep):
        cans = robbyWorld.gencans()
        world = robbyWorld.genworld(cans)
        myStrategy = [4, 4, 6, 1, 2, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 0, 0, 6, 0, 0, 6,
                      3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6,
                      1, 1, 6, 1, 1, 6, 1, 1, 6, 2, 2, 6, 2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6,
                      2, 2, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 3, 3, 6, 3, 3, 6, 3, 3, 6, 5, 5, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6,
                      2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 0, 0, 6,
                      0, 0, 6, 3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6,
                      0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6,
                      3, 3, 6, 2, 2, 6, 2, 2, 6, 4, 4, 6]

        x = 0
        y = 0

        north = world[x, y].north
        south = world[x, y].south
        west = world[x, y].west
        east = world[x, y].east
        current = world[x, y].current

        assert north == 1
        assert south != 1
        assert west == 1
        assert east != 1
        assert current != 1

        index = 3 ** 0 * current + 3 ** 1 * east + 3 ** 2 * west + 3 ** 3 * south + 3 ** 4 * north

        action = myStrategy[index]
        assert action == 1 or action == 3 or action == 6

        [x, y, score] = robbyActions.locationAndScore(world, x, y, action)
        if action == 1:
            assert x == 0
            assert y == 1
            assert score >= 0
            assert world[1, 0].current == 0  # Verify no can in East square
        elif action == 3:
            assert x == 1
            assert y == 0
            assert score >= 0
            assert world[1, 0].current == 2  # Verify there is a can in East square
        elif action == 6:
            assert x == 0
            assert y == 0
            assert score >= 2
            assert world[0, 0].current == 0  # After picking up the can, the square is now empty


# Testing totalScore(world, strategy) function for calculating the correct score for myStrategy
def testTotalScore():
    for i in range(params.nrep):
        cans = robbyWorld.gencans()
        world = robbyWorld.genworld(cans)
        myStrategy = [4, 4, 6, 1, 2, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 0, 0, 6, 0, 0, 6,
                      3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6,
                      1, 1, 6, 1, 1, 6, 1, 1, 6, 2, 2, 6, 2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6,
                      2, 2, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 3, 3, 6, 3, 3, 6, 3, 3, 6, 5, 5, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6,
                      2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 0, 0, 6,
                      0, 0, 6, 3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6,
                      0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6,
                      3, 3, 6, 2, 2, 6, 2, 2, 6, 4, 4, 6]
        score = robbyActions.totalScore(world, myStrategy)

        assert score >= 0


# Testing scoreavg(strategy) function for calculating the correct score for myStrategy
def testAvgScore():
    for i in range(params.nrep):
        myStrategy = [4, 4, 6, 1, 2, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 0, 0, 6, 0, 0, 6,
                      3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6,
                      1, 1, 6, 1, 1, 6, 1, 1, 6, 2, 2, 6, 2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6,
                      2, 2, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 3, 3, 6, 3, 3, 6, 3, 3, 6, 5, 5, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6,
                      2, 2, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 2, 2, 6, 0, 0, 6,
                      0, 0, 6, 3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 0, 0, 6, 0, 0, 6, 3, 3, 6,
                      0, 0, 6, 0, 0, 6, 3, 3, 6, 2, 2, 6, 2, 2, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6, 3, 3, 6, 1, 1, 6, 1, 1, 6,
                      3, 3, 6, 2, 2, 6, 2, 2, 6, 4, 4, 6]
        myScore = robbyActions.scoreavg(myStrategy)

        assert myScore >= 0


# ==========   Crossover Tests   ==========

# Testing mutate(P1) to verify random mutation in myStrategy
def testMutate():
    myStrategy = np.random.randint(0, 7, 3 ** 5)
    myStrategyMutated = crossover.mutate(myStrategy)
    diff = myStrategyMutated - myStrategy

    assert np.count_nonzero(diff) >= params.nmutations


# Testing crossover(P1, P2) to verify crossover between two strategies provides npop children
def testCrossOver():
    P1 = np.random.randint(1, 7, 3 ** 5)  # Generated without action '0' to simplify nozero count
    P2 = np.random.randint(1, 7, 3 ** 5)  # Generated without action '0' to simplify nozero count
    pop = crossover.crossover(P1, P2)

    assert len(pop) == params.npop

    C1 = pop[0]
    assert len(C1) == 3**5

    diff1 = C1 - P1  # Contribution of P1 to C1
    diff2 = C1 - P2  # Contribution of P2 to C1
    assert (3**5 - np.count_nonzero(diff1)) + (3**5 - np.count_nonzero(diff2) >= len(C1))

    Crand = pop[np.random.randint(0, params.npop)]
    assert len(Crand) == 3 ** 5

    diff1 = Crand - P1
    diff2 = Crand - P2
    assert (3**5 - np.count_nonzero(diff1)) + (3**5 - np.count_nonzero(diff2)) >= len(Crand)
