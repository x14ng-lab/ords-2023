import setup
import selection as slc
import crossover as co
import mutation as mu


def next_generation(num_generations, population, original_matrix, target_row_sums, target_col_sums, tournament_size, mutation_rate):
    '''
    Combine the offspring to form a new population, which then 
    undergoes the same process of selection, crossover, and mutation.

    Input: 
        num_generations (int), the maximum number of generations to run the GA.
        population (list), the initial population of potential solutions.
        original_matrix (array), the original randomly generated Sumplete game board.
        target_row_sums (array), an array of the target row sums.
        target_col_sums (array), an array of the target column sums.
        tournament_size (int), the number of individuals participating in 
            each tournament selection event.
        mutation_rate (float), the probability of mutation occurring in an individual.
    
    Output:
        population (list), the final population.
        num_generations (int), the number of generations it ran for.
    '''
    # Iterate through each generation
    for generation in range(num_generations):
        # Calculate the fitness scores for each individual in the current population
        fitnesses = setup.calculate_fitnesses(population, original_matrix, target_row_sums, target_col_sums)

        # Select the parents for the next generation through the tournament selection process
        selected_individuals = slc.tournament_selection(population, fitnesses, tournament_size)

        # Initialise a list to store the new offsprings
        offspring = []

        # Iterate through the selected individuals by pairs for crossover and mutation
        for i in range(0, len(selected_individuals), 2):
            if i < len(selected_individuals) - 1:
                offspring1, offspring2 = co.crossover(selected_individuals[i], selected_individuals[i+1])
                offspring.append(mu.mutation(offspring1, mutation_rate))
                offspring.append(mu.mutation(offspring2, mutation_rate))

        # Replace the old population with the new offspring
        population = offspring 

        # Check for a correct solution
        if max(fitnesses) == 1:
            print(f"Solution found at generation {generation}")
            return population, generation

    # If no solution is found
    print("No solution found within the given number of generations.")
    return population, num_generations