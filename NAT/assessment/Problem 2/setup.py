import numpy as np


# Original Matrix Generation
def original_matrix_generator(k):
    '''
    Create a kxk matrix of random integers between 1 and 9 to simulate a Sumplete game board.

    Input: 
        k (int), the size of the matrix.
    
    Output:
        original_matrix (array), a randomly generated Sumplete game board.
    '''
    np.random.seed(0)  # For reproducibility
    original_matrix = np.random.randint(1, 10, size=(k, k))
    return original_matrix

# Generate Random Target Sums
def generate_target_sums(original_matrix, deletion_rate):
    '''
    Generate random target row and column sums

    Input:
        original_matrix (array), a randomly generated Sumplete game board.
        deletion_rate (int), the deletion rate of the game.
    '''
    k = original_matrix.shape[0]

    # Copy the original matrix to not alter it
    matrix_copy = np.copy(original_matrix)

    # Calculate the number of deletions for the entire matrix
    total_entries = k * k
    num_deletions = int(np.ceil(total_entries * deletion_rate))
    
    # Generate indices for the deletions
    deletion_indices = np.random.choice(total_entries, num_deletions, replace=False)
    
    # Flatten the matrix copy and set deletions
    matrix_copy.flat[deletion_indices] = 0

    # Calculate the target row and column sums from the modified matrix
    target_row_sums = np.sum(matrix_copy, axis=1)
    target_col_sums = np.sum(matrix_copy, axis=0)

    return target_row_sums, target_col_sums


# Population Initialisation
def initialise_population(pop_size, matrix_size, deletion_rate):
    '''
    Initialise the GA population.

    Input:
        pop_size (int), the population size.
        matrix_size (int), the size of the matrix.
        deletion_rate (int), the deletion rate.

    Output:
        population (list), a list of binary matrices,
            each representing a individual in the popluation
    '''
    # Initialise an empty list to store all individuals of the initial population 
    population = []

    # Calculate the number of cells to delete from each individual matrix
    num_deletions = int(matrix_size * matrix_size * deletion_rate)

    # Iterate 'pop_size' times to create the same number of individuals as our population size
    for _ in range(pop_size):
        # Initialise an individual solution as a matrix filled with ones
        individual = np.ones((matrix_size, matrix_size), dtype=int)

        # Randomly select positions in the individual matrix for later deletions
        deletions = np.random.choice(matrix_size * matrix_size, num_deletions, replace=False)

        # Set the positions selected in the previous step to zero
        individual.flat[deletions] =  0

        # Add the modified individual matrix to the population list
        population.append(individual)

    return population


# Fitness Function: Binary fitness function
def fitness_function(matrix, original_matrix, target_row_sums, target_col_sums):
    '''
    Check if the modified matrix's row and column sums match the target sums.

    Input:
        matrix (array), an individual solution from the population,
            a k-by-k binary matrix where each entry is either 1 or 0.
        original_matrix (array), the original randomly generated Sumplete game board.
        target_row_sums (array), an array of the target row sums.
        target_col_sums (array), an array of the target column sums.
    
    Output:
        binary output
    '''
    # Calculate the row sums and column sums of the modified matrix
    row_sums = np.sum(matrix * original_matrix, axis=1) 
    col_sums = np.sum(matrix * original_matrix, axis=0)

    # Check if the sums match the target sums
    if np.array_equal(row_sums, target_row_sums) and np.array_equal(col_sums, target_col_sums):
        return 1
    else:
        return 0


# Fitnesses Calculation
def calculate_fitnesses(population, original_matrix, target_row_sums, target_col_sums):
    '''
    Calculate the fitness for each individual in the population.

    Input:
        population (list), the entire group of individuals of the 
            current generation within the genetic algorithm. 
        original_matrix (array), the original randomly generated Sumplete game board.
        target_row_sums (array), an array of the target row sums.
        target_col_sums (array), an array of the target column sums.

    Output:
        a list of calculated fitness values.
    '''
    return [fitness_function(individual, original_matrix, target_row_sums, target_col_sums) for individual in population]