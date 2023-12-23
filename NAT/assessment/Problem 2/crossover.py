import numpy as np


def crossover(parent1, parent2):
    '''
    Perform 1-point crossover operation on two parent individuals from the population.

    Input:
        parent1, parent2 (array), the first and second parent individual 
            selected from the population to undergo crossover.
    
    Output:
        offspring1, offspring2 (array), the two new offspring matrices 
            that combine genetic material from both parents at the
            'crossover_point'.
    '''
    # Initialise copies of 'parent1' and 'parent2' for modifications
    offspring1 = parent1.copy()
    offspring2 = parent2.copy()

    # Generate a random index to determine where the crossover occur
    crossover_point = np.random.randint(1, parent1.shape[0] * parent1.shape[1])

    # Perform the crossover
    offspring1.flat[crossover_point:] = parent2.flat[crossover_point:]
    offspring2.flat[crossover_point:] = parent1.flat[crossover_point:]

    # Return the two new offspring matrices
    return offspring1, offspring2
