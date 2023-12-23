import numpy as np
import ballot_data as bd
import irv

def stv_results(ballots, seats):
    '''
    Calculate the election result using the single transferable vote system.

    Input:
        ballots (numpy.ndarray): a NumPy array containing ballot data, 
            with one row per ballot and one column per candidate.
        seats (int): the number of seats up for election.

    Output:
        elected (list): a list of elected candidates in the order of being elected.
        eliminated (list): a list of eliminated candidates in the order of being eliminated.
    '''
    # Check that the input arguments are valid
    if not (isinstance(ballots, list) or isinstance(seats, int)):
        raise TypeError('Please enter a n-D array for ballots and an integer for seats.')
    
    # Count the number of voters and candidates
    num_voters, num_candidates = ballots.shape

    # Initialise the list of elected and eliminated candidates
    elected = []
    eliminated = []

    # Calculate the required quota of valid first-preference votes (number 1 cannot be repeated in a ballot)
    quota = num_voters // (seats + 1) + 1

    # Initialise a list to store the votes in different iteration
    votes = np.zeros(num_candidates, dtype=float)

    # Define a new function for redistributing the votes if eliminating the "candidate"
    def redistribute_votes(candidate, weighting=1):
        for ballot in ballots:
            if ballot[candidate] == 1:
                # Finds the indices of all candidates who were the second preference on this ballot
                next_choice = np.where(ballot == 2)[0]
                if next_choice.size > 0:
                    votes[next_choice[0]] += weighting
                # Set the vote for this candidate to 0 and avoid double counting
                ballot[candidate] = 0
                # Upgrade the preference for the other candidates
                ballot[ballot > 1] -= 1

    while len(elected) < seats:
        # Calculate the first-preference votes for each candidate
        for i in range(num_candidates):
            if i not in elected and i not in eliminated:
                votes[i] = np.sum(ballots[:, i] == 1)

        # Check if any candidate surpasses the quota
        for i in range(num_candidates):
            if votes[i] >= quota:
                elected.append(i)
                weighting = (votes[i] - quota) / votes[i]
                redistribute_votes(i, weighting)
                votes[i] = 0  # Set their votes to 0 as they are elected
                break

        # If no one meets te quota, eliminate the least popular candidate
        if len(elected) < seats:
            # Find any candidate that is either elected or eliminated (ineligible)
            ineligible_candidates = np.isin(range(num_candidates), elected + eliminated)
            # Find the lowest vote count for any candidate that has not been elected or eliminated (eligible)
            min_votes = np.min(votes[np.logical_not(ineligible_candidates)])
            # Find the indices of all the candidates with the lowest vote
            candidates_with_min_votes = np.where(votes == min_votes)[0]

            # In case of a tie, we choose the first candidate to eliminate
            to_eliminate = candidates_with_min_votes[0]
            eliminated.append(to_eliminate)
            redistribute_votes(to_eliminate)
            votes[to_eliminate] = 0 # Set their votes to 0 as they are eliminated

        # If we have filled all seats, break the loop
        if len(elected) == seats:
            break

    # Fill the eliminated list if seats are filled before all eliminations
    while len(eliminated) < num_candidates - seats:
        remaining = [i for i in range(num_candidates) if i not in elected + eliminated]
        eliminated.append(remaining[0]) # Eliminate the candidate with the smallest index
    
    # Return the outputs
    return elected, eliminated
