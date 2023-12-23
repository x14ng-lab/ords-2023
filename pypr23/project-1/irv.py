import numpy as np
import ballot_data as bd

def find_least_popular(ballots, eliminated):
    '''
    Find the next candidate to eliminate.

    Input:
        ballots (numpy.ndarray): a NumPy array containing ballot data, 
            with one row per ballot and one column per candidate.
        eliminated (list): a list of previously eliminated candidates (indices).

    Output:
        int: index of the next candidate to eliminate.
    '''
    # Check that the input arguments are valid
    if not (isinstance(ballots, list) or isinstance(eliminated, list)):
        raise TypeError('Please enter a n-D array for ballots and a list for eliminated.')
    
    # Count the number of voters and candidates
    num_voters, num_candidates = ballots.shape

    # Create a list of remaining candidates (not eliminated)
    remaining_candidates = [i for i in range(num_candidates) if i not in eliminated]

    # Initialise a dictionary to store the tally of first preference for remaining candidates
    first_preference_counts = {candidate: 0 for candidate in remaining_candidates}

    # Tally the first preference for each of the candidate
    rank = 1
    for candidate in remaining_candidates:
        # Reshape the one-dimensional array into a two-dimensional array (because of my setting of tally_preferences())
        candidate_preferences = ballots[:, [candidate]]

        # Use tally_preferences() to count the first preference for the current candidate (1 indicates first preference)
        preferences = bd.tally_preferences(candidate_preferences, rank)

        # Store the count in first_preference_counts dictionary
        first_preference_counts[candidate] = preferences[0]

    # Find the candidate(s) with the fewest first preference
    min_first_preference_count = min(first_preference_counts.values())
    least_popular_candidates = [candidate for candidate, count in first_preference_counts.items() if count == min_first_preference_count]

    # If there's no tie, return the least popular candidate
    if len(least_popular_candidates) == 1:
        return least_popular_candidates[0]
    
    # If there's a tie, resolve it by looking at subsequent preferences
    while len(least_popular_candidates) > 1 and rank <= num_candidates:
        next_preference_count = {candidate: 0 for candidate in least_popular_candidates}

        # Tally the next preference for tied candidates
        for candidate in least_popular_candidates:
            candidate_preferences = ballots[:, [candidate]]
            preferences = bd.tally_preferences(candidate_preferences, rank)
            next_preference_count[candidate] = preferences[0]
        
        # Find the candidate(s) with the fewest next preferences
        min_next_preference_count = min(next_preference_count.values())
        least_popular_candidates = [candidate for candidate, count in next_preference_count.items() if count == min_next_preference_count]

        # Increase the rank for the next loop iteration
        rank += 1

    # After breaking ties or if there's a tie at the last preference, eliminate the candidate with the smallest index
    return min(least_popular_candidates)



def update_ballots(ballots, to_eliminate):
    '''
    Eliminate the least popular candidate and return the updated ballot (after redistributing).

    Input:
        ballots (numpy.ndarray): a NumPy array containing ballot data, 
            with one row per ballot and one column per candidate.
        to_eliminate (int): index of the candidate to eliminate this round.
    
    Output:
        ballots (numpy.ndarray): updated ballot data.
    '''
    # Check that the input arguments are valid
    if not (isinstance(ballots, list) or isinstance(to_eliminate, int)):
        raise TypeError('Please enter a n-D array for ballots and an integer for to_eliminate.')
    
    # Count the number of voters and candidates
    num_voters, num_candidates = ballots.shape

    for i in range(num_voters):
        # Iterate through all the ballots to decide on their modification
        for j in range(num_candidates):
            # Exclude the eliminated candidate
            if j != to_eliminate:
                # Check if the eliminated candidate received any preference in this ballot
                if ballots[i, to_eliminate] != 0:
                    # Upgrade the preference rank for candidates who ranked below
                    if ballots[i, j] > ballots[i, to_eliminate]:
                        ballots[i, j] -= 1
        
        # Unrank the eliminated candidate's preference in this ballot
        ballots[i, to_eliminate] = 0

    # Return the updated ballot data
    return ballots

            

def calculate_results(ballots):
    '''
    Run the election.
    
    Input:
        ballots (numpy.ndarray): a NumPy array containing ballot data, 
            with one row per ballot and one column per candidate.
    
    Output:
        winner (int): index of the winner.
        eliminated (list): a list of the eliminated candidates in the 
            order_
              they were eliminated.
    '''
    # Initialise the eliminated list
    eliminated = []

    # Create a winner list where 1 represent the candidate is in the list; 0 otherwise
    winner = [1 for i in range(ballots.shape[1])]

    while True:
        # Find the next candidate to eliminate
        to_eliminate = find_least_popular(ballots, eliminated)

        # Eliminate this candidate and update the ballot (after redistributing)
        ballots = update_ballots(ballots, to_eliminate)

        # Append this candidate to the eliminated list
        eliminated.append(to_eliminate)
        
        # Remove this candidate from the winner list
        winner[to_eliminate] -= 1

        # Iterate until the winner has been selected
        if sum(winner) == 1:
            break
    
    # Return the winner and the eliminated list
    return winner.index(1), eliminated