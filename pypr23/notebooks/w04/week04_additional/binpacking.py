def first_fit(items, bin_capacity):
    '''
    First-fit heuristic for the bin packing problem.
    Takes in a list of items of different sizes, and a bin capacity.
    Returns a list of bins and how much they each contain.
    '''
    # Initialise a list of bins
    bins = []

    # Loop over the list of items
    for i in items:
        # Item starts not being placed in a bin
        placed = False

        # Loop over the bins (until we find a good one)
        for b in range(len(bins)):
            # Check bin 0; does i fit?
            if bin_capacity - bins[b] >= i:
                # Yes, there is enough space; add current item to the bin
                bins[b] += i
                placed = True
                # Move on to the next item
                break
        
        if not placed:
        # if placed == False:
            # Open a new bin
            bins.append(0)
            bins[-1] += i
        

    # Return the result
    return bins



# Testing our function
items = [2, 1, 3, 2, 1, 2, 3, 1]
bin_capacity = 4
bins = first_fit(items, bin_capacity)
print(bins)  # expected: [4, 4, 4, 3]
