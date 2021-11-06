"""
Crossover:
P1 - parent1 (243 long array)
P2 - parent2 (243 long array)
Cut P1 at a random index and add to it the complementary len-index from P2 to create C1
Cut P1 at a different random index and add to it the complementary len-index from P2 to create C2
...
So on until C200 to keep the population at 200

Mutate:
Select randomly N indices from each child and mutate randomly
"""

import numpy as np
import params


def mutate(P1):
    P1Mutated = np.copy(P1)
    diff = P1Mutated - P1
    while np.count_nonzero(diff) <= params.nmutations:
        index = np.random.randint(0, 3 ** 5)
        P1Mutated[index] = np.random.randint(0, 7)
        diff = P1Mutated - P1
    return P1Mutated


def crossover(P1, P2):
    pop = list()
    for i in range(params.npop//2):
        index = np.random.randint(0, 3**5)
        C1P1 = P1[0:index]
        C1P2 = P2[index:3**5]
        C1 = np.append(C1P1, C1P2)
        pop.append(mutate(C1))
        C2P2 = P2[0:index]
        C2P1 = P1[index:3**5]
        C2 = np.append(C2P2, C2P1)
        pop.append(mutate(C2))
    return pop
