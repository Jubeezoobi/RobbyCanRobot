"""
Initializing 2 opening strategies
Crossover function takes these 2 strategies and return a population of params.npop strategies
Calculating score for each strategy and picking the best 2
The best 2 spawn the next generation
"""

import numpy as np
import csv
import params
import robbyActions
import crossover

# Initializing two opening strategies
P1 = np.random.randint(0, 7, 3 ** 5)
P2 = np.random.randint(0, 7, 3 ** 5)
scoreP1 = -500
scoreP2 = -500

# With P1 and P2 initialized, starting to crossover and making new population each generation.
# Running for params.ngen generations.
printGate = -50
for gen in range(params.ngen):
    pop = crossover.crossover(P1, P2)
    for i in range(params.npop):
        strategy = pop[i]
        score = robbyActions.scoreavg(strategy)
        if (score >= scoreP1) and (score >= scoreP2):
            P1 = strategy
            scoreP1 = score
        elif (score <= scoreP1) and (score >= scoreP2):
            P2 = strategy
            scoreP2 = score

    if scoreP2 >= printGate:
        print(f"GEN{gen} P1 Score: ", scoreP1)
        print(f"GEN{gen} P2 Score: ", scoreP2)
        printGate += 10

print(f"GEN{gen} best strategy:")
print(P1)

# Write the best strategy to a text file
with open('Strategies/gaStrategy.csv', 'w', newline='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter=' ')
    my_writer.writerow(P1)
