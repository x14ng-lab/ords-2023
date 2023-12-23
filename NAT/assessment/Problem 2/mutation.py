import numpy as np


def mutation(individual, mutation_rate):
    '''
    Introduce random changes to individuals.

    Input:
        individual (array), the individual solution to apply the mutation.
        mutation_rate (float), the probability of mutation occurring in an individual.
    
    Output:
        individual (array), the individual solution after being mutated.

    '''
    # Create a random boolean matrix for mutation
    mutation_indices = np.random.rand(*individual.shape) < mutation_rate

    # Perform the mutation (flip the value of each entry selected to mutate)
    individual[mutation_indices] = 1 - individual[mutation_indices]

    # Return the mutated individual
    return individual
