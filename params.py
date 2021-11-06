"""
World parameters for robbyWorld
Action parameters for robbyActions and score
Genetic algorithm parameters for generations and population
"""

# World parameters
xsize = 10  # X axis of robbyWorld
ysize = 10  # Y axis of robbyWorld
nofcans = 20  # Number of cans in robbyWorld

# Robby's actions parameters
nofsteps = 100  # Number of steps Robby is allowed to take in robbyActions
scoreCan = 25  # Score for picking up a can
scoreWall = -5  # Score for crashing into a wall
scoreNoCan = -1  # Score for trying to pick a can where there is no can

# GA parameters
nrep = 20  # Number of boards each strategy is tested against
npop = 50  # Number of strategies in a population
ngen = 100  # Number of generations
nmutations = 3  # Number of mutations in crossover function
