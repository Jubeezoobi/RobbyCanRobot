# RobbyCanRobot
Implementation for Melanie Mitchell's Robby the Can Robot as described in her book 'Complexity - A Guided Tour'

A Python implementation for genetics (evolutionary) algorithm that attemps to find optimal strategy for Robby to pick 20 cans randomly set on a 10x10 board.
The genetic algorithm (GA) randomly selects a population of 200 strategies and tests each on 50 boards (those are parameters in params.py)
The best 2 strategies are selected as parents for the next generation of strategies, in each generation 3 mutations are randomly done in each strategy.

As Robby can only 'see' its current square + 1 square in each direction (north, south, east and west) and each square can be either 'can', 'no can' or 'wall',
a strategy consists of 3^5 possible moves that Robby can take.

The possible moves for Robby as well as the score function are all detailed as comments within the code.

Thanks to Melanie Mitchell for the inspiration and for a very interesting read, I really recommend for anyone taking interest in order emerging from chaos to read her book.
