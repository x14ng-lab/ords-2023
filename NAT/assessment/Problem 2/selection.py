import numpy as np


def tournament_selection(population, fitnesses, tournament_size):
    '''
    Selection function using tournament selection.

    Input:
        population (list), the current population of individuals.
        fitnesses (list), the fitness scores corresponding to each individual in the population.
        tournament_size (int), the number of individuals participating in 
            each tournament selection event.
    
    Output:
        selected_individuals (list), a list of parents.
    '''
    # Initialise an empty list to store the individuals selected to be parents
    selected_individuals = []

    # Iterate once for each individual and select one to be a parent
    for _ in range(len(population)):
        # Select 'tournament_size' random indices from the population without replacement for the tournament
        tournament_indices = np.random.choice(len(population), tournament_size, replace=False)

        # Create a list for the selected individuals
        tournament_individuals = [population[i] for i in tournament_indices]

        # Create a list to store the fitness values for the selected individuals 
        tournament_fitnesses = [fitnesses[i] for i in tournament_indices]

        # Find the index of the individual with the highest fitness in the tournament
        winner_index = tournament_indices[np.argmax(tournament_fitnesses)]

        # Add the winning individual to the list of selected parents
        selected_individuals.append(population[winner_index])

    return selected_individuals

