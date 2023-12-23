import numpy as np
import rastrigin as rf


# Define the PSO parameters
class PSOParameters:
    def __init__(self, particle_size, dimensions, inertia_weight, cognitive_constant, social_constant, function_evaluations):
        self.particle_size = particle_size
        self.dimensions = dimensions
        self.inertia_weight = inertia_weight
        self.cognitive_constant = cognitive_constant
        self.social_constant = social_constant
        self.function_evaluations = function_evaluations


# Initialise the swarm
def initialise_swarm(pso_params):
    '''
    Initialise the swarm with random positions and velocities, sets the initial personal 
    best positions and scores, and identifies the initial global best position and score.

    Input:
        pso_params (PSOParameters), a class instance containing all the PSO parameters.
            - particle_size, number of particles in the swarm.
            - dimensions, number of dimensions of the search space (problem difficulty).
            - inertia_weight, inertia weight to control the influence of the previous velocity.
            - cognitive_constant, cognitive parameter to control the influence of the particle's personal best position.
            - social_constant, social parameter to control the influence of the swarm's global best position.
            - function_evaluations, total number of allowed evaluations of the cost function.
    
    Output:
        tuple, contains the following initialised values for the swarm:
            - swarm_positions, a 2D array where each row represents a particle's position.
            - swarm_velocities, a 2D array where each row represents a particle's velocity.
            - personal_best_positions, a 2D array where each row represents the best position a particle has visited.
            - personal_best_scores, a array containing the best score for each particle.
            - global_best_position, the best position found across all particles.
            - global_best_score, the score of the best position found across all parricles.
    '''
    # Each particle's position and velocity are randomly initialised
    # np.random.seed(0) for plotting
    swarm_positions = np.random.uniform(-5.12, 5.12, (pso_params.particle_size, pso_params.dimensions))
    swarm_velocities = np.random.uniform(-1, 1, (pso_params.particle_size, pso_params.dimensions))
    personal_best_positions = np.copy(swarm_positions)
    personal_best_scores = np.array([rf.rastrigin_func(position) for position in swarm_positions])
    global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
    global_best_score = np.min(personal_best_scores)
    
    return swarm_positions, swarm_velocities, personal_best_positions, personal_best_scores, global_best_position, global_best_score


# Define the PSO main loop function
def run_pso(pso_params):
    '''
    Run the Particle Swarm Optimisation (PSO) algorithm with a specified set of parameters.

    Input:
        pso_params (PSOParameters), a class instance containing all the PSO parameters.
    
    Output:
        float, the best score achieved by the swarm after running the PSO algorithm.
    '''
    # Initialise the swarm with random positions and velocities
    swarm_positions, swarm_velocities, personal_best_positions, personal_best_scores, global_best_position, global_best_score = initialise_swarm(pso_params)
    evaluations = 0  # counter for the number of function evaluations
    
    # Main loop of PSO that runs until the maximum number of function evaluations is reached
    while evaluations < pso_params.function_evaluations:
        # Iterate over all particles in the swarm
        for i in range(pso_params.particle_size):
            r1, r2 = np.random.rand(2)  # stochastic coefficients

            # Update the velocity of the particle
            swarm_velocities[i] = (pso_params.inertia_weight * swarm_velocities[i] +
                                   pso_params.cognitive_constant * r1 * (personal_best_positions[i] - swarm_positions[i]) +
                                   pso_params.social_constant * r2 * (global_best_position - swarm_positions[i]))
            
            # Update the position of the particle
            swarm_positions[i] += swarm_velocities[i]
            
            # Ensure the particle's position is within the defined bounds
            swarm_positions[i] = np.clip(swarm_positions[i], -5.12, 5.12)
            
            # Evaluate the new position's fitness
            fitness = rf.rastrigin_func(swarm_positions[i])
            evaluations += 1 # increment the evaluation counter

            # Update the particle's personal best if the new fitness is better
            if fitness < personal_best_scores[i]:
                personal_best_scores[i] = fitness
                personal_best_positions[i] = swarm_positions[i]
        
        # Find the best fitness in the swarm and update the global best if it's better than the current global best
        min_personal_best_score = np.min(personal_best_scores)
        if min_personal_best_score < global_best_score:
            global_best_score = min_personal_best_score
            global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
    
    # Return the best score found by the swarm
    return global_best_score