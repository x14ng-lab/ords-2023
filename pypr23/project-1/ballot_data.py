import numpy as np

def generate_ballots(votes=100, candidates=6, target_results=[30, 27, 21, 13, 6, 3]):
    '''
    Generate random ballot data given a total number of ballots (votes),
    a total number of candidates, and a target probability distribution
    of preferences.
    The probabilities are randomly attributed to each candidate for each
    level of preference.
    
    Returns a NumPy array with shape (votes, candidates), where each row
    is one ranked-choice ballot for one voter, and each column corresponds
    to one candidate.
    '''
    # Initialise a random number generator
    rng = np.random.default_rng()
    
    # Set target probabilities for each stage (normalised)
    prob = np.array(target_results, dtype=float)
    prob = np.tile(prob, (candidates, 1))
    # shuffle probabilities so they're applied differently for each rank; add some noise too
    prob = np.abs(rng.permuted(prob, axis=1) + rng.normal(scale=2, size=prob.shape))
    
    # Create an empty array to store the ballots
    ballots = np.zeros((votes, candidates))
    
    # Create each ballot one after the other
    for v in range(votes):
        # Voter ranks at most "candidates" candidates; introduce "stages" for clarity
        stages = candidates
        for r in range(stages):
            
            # Generates rth preference for an arbitrary candidate (use normalised probabilities)
            chosen_candidate = rng.choice(candidates, p=prob[r, :]/prob[r, :].sum())
            
            if ballots[v, chosen_candidate-1] > 0:
                # Arbitrarily decide that voter is done if they choose the same candidate twice
                break
            else:
                # If they hadn't previously chosen that candidate, choose it as rth preference (r indexes from 0)
                ballots[v, chosen_candidate-1] = r + 1
    
    return ballots


def select_ballots(ballots, rank, candidate):
    '''
    Returns a selector for all ballots which have allocated a given rank to a given candidate.
    '''
    # Create a bool mask: look at one candidate's column,
    # and find all the rows where that candidate's rank is rank
    return ballots[:, candidate] == rank


def tally_preferences(ballots, rank):
    '''
    Tally the total number of preferences at the given rank for each candidate.

    Input:
        ballots (numpy.ndarray): a NumPy array containing ballot data, 
            with one row per ballot and one column per candidate.
        rank (int): an integer between 1 and the total number of candidates (inclusive).
    
    Output:
        preferences (list): a list of the same length as the total number of candidates, 
            containing the total number of preferences at the given rank for each candidate.
    
    This function takes a 2D array of ballots and a rank, and returns a list with the total
    number of preferences each candidate received at that rank.
    '''
    # Count the number of voters and candidates
    num_voters, num_candidates = ballots.shape

    # Check that the input arguments are valid
    if not (isinstance(ballots, list) or isinstance(rank, int)):
        raise TypeError('Please enter a n-D array for ballots and an integer for n.')

    if rank < 1:
        raise ValueError('Please choose a value of rank between 1 and the total number of candidates.')

    # Initialise an empty list to store the count of preferences
    preferences = [0] * num_candidates
    
    # Iterate through each candidate and count the number of preference at the given rank
    for candidate in range(num_candidates):
        for voter in range(num_voters):
            if ballots[voter, candidate] == rank:
                preferences[candidate] += 1
    
    return preferences