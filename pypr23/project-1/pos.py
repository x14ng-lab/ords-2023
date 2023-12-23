import numpy as np
import matplotlib.pyplot as plt
import ballot_data as bd

def positional_voting(ballots, weights):
    '''
    Tally the total number of points obtained by each candidate 
    using the positional voting system with a given weighting scheme.

    Input:
        ballots (numpy.ndarray): a NumPy array containing ballot data, 
            with one row per ballot and one column per candidate.
        weights (list): a list of the same length as the total number of candidates, 
            containing the weights attributed to each preference rank in decreasing order.
    
    Output:
        results (list): a list of the same length as the total number of candidates, 
            containing the total number of points obtained by each candidate using the weights.

    This function calculates the total points obtained by each candidate in a positional voting system
    with a given weighting scheme based on the preferences expressed in the ballots.
    '''
    # Count the number of candidates
    num_candidates = ballots.shape[1]

    # Check that the input arguments are valid
    if not (isinstance(ballots, list) or isinstance(weights, list)):
        raise TypeError('Please enter a n-D array for ballots and a list for weights.')

    if len(weights) != (num_candidates):
        raise ValueError("Please set the length of list 'weights' the same as the total number of candidates.")
    
    # Get the total number of rank
    num_rank = num_candidates

    # Initialise an empty list to store the count of points
    results = [0] * num_candidates

    # Iterate through each rank and count the number of points obtained by each candidate
    for rank in range(num_rank):
        preferences = bd.tally_preferences(ballots, rank + 1)
        for candidate in range(num_candidates):
            results[candidate] += preferences[candidate] * weights[rank]
    
    return results


def display_results(ballots, weight_sets):
    '''
    Display bar charts indicating the overall score for each candidate 
    based on different weighting schemes.

    Input:
        ballots (numpy.ndarray): a NumPy array containing ballot data, 
            with one row per ballot and one column per candidate.
        weight_sets (list): a list containing N different weighting schemes. 
            Each weighting scheme is a list of weights.
    
    This function creates a figure with N subplots, each showing a bar chart
    of the overall scores for each candidate under different weighting schemes.
    '''
    # Check that the input arguments are valid
    if not (isinstance(ballots, list) or isinstance(weight_sets, list)):
        raise TypeError('Please enter a n-D array for ballots and a list for weight_sets.')
    
    # Count the number of candidates
    num_candidates = ballots.shape[1]

    # Get the total number of weighting schemes
    num_weights = len(weight_sets)

    # Create figure and axes
    fig, axes = plt.subplots(num_weights, 1, figsize=(8, 5 * num_weights))

    # Create the labels for the bar chart
    candidates = [f'Candidate {i}' for i in range(1, num_candidates + 1)]

    # Iterate throught each weighting scheme and plot the corresponding bar chart
    for i, weights in enumerate(weight_sets):
        # Calculate the overall score of each candidate under the current weighting scheme
        overall_scores = positional_voting(ballots, weights)

        # Find the index of the candidate with the highest overall score
        highest_score_index = overall_scores.index(max(overall_scores))

        # Define colors for the bars, highlighting the winner
        colors = ['orange' if j == highest_score_index else 'grey' for j in range(num_candidates)]

        # Plot the bar chart for the current weighting scheme
        axes[i].bar(candidates, overall_scores, color=colors)
        axes[i].set_ylabel('Overall Score')
        axes[i].set_title(f'Weighting Scheme {i + 1}')
    
    # To ensure the plots are spaced properly
    plt.tight_layout()
    
    # Display the plots
    plt.show()

