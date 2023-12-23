import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Set up a random list of integers
n = 1000
rng = np.random.default_rng()
my_list = rng.integers(1, n+1, size=n)

def bubble_sort(arr):
    '''
    Sorts the list or array arr using bubble sort.

    Input: arr (list or array): the array to sort
    Output: sorted_arr (list): a copy of arr, with elements sorted in order
    '''
    # Make a copy first
    sorted_arr = arr.copy()
    counter = 1

    # Keep looping over the list until there are no more swaps
    while True:
        # Keep track of whether we've swapped anything this time
        swapped = False

        # Compare each consecutive pair of elements
        for i in range(len(sorted_arr)-counter):
            if sorted_arr[i] > sorted_arr[i+1]:
                # Swap!
                sorted_arr[i], sorted_arr[i+1] = sorted_arr[i+1], sorted_arr[i]
                swapped = True

        # The next largest element is now at the correct place, we don't need to check it anymore
        counter += 1

        # If at this point swapped is still False, we can finish
        if not swapped:
            return sorted_arr

my_list_bubble = bubble_sort(my_list)
my_list_sorted = sorted(my_list)
print(np.all(my_list_bubble == my_list_sorted))

# Time bubble_sort
def time_sort(sort_function, lengths, repeat=1):
    '''
    Measures the time taken by sort_function to sort large lists.

    Input:
        sort_function (function): the function to benchmark
        lengths (list or array): list of array sizes to generate
        repeat (int): run the algorithm several times per array,
            compute average time over multiple runs
    '''
    # Set up RNG
    rng = np.random.default_rng()

    # Keep track of the times
    times = []
    for n in lengths:
        # Set up the array
        arr = rng.integers(1, n+1, size=n)

        # Run sort_function and time it 5 times
        t = 0
        for i in range(repeat):
            t0 = time.time()
            sort_function(arr)
            t += time.time() - t0
        times.append(t / repeat)

    return lengths, times


lengths, times = time_sort(bubble_sort, range(500, 3001, 500))

# Plot the results
fig, ax = plt.subplots(1, 2)
ax[0].plot(lengths, times, 'kx')
ax[0].set_xlabel('Array size')
ax[0].set_ylabel('Execution time (s)')
ax[1].plot(np.log(np.array(lengths)), np.log(np.array(times)), 'kx')
plt.show()

# Merge sort
def merge(arr1, arr2):
    '''
    Merge 2 sorted lists into one sorted list.
    '''
    sorted_list = []

    # Loop until the full list is formed, start at index 0 for both lists
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        # Compare the items at the current locations for both lists
        if arr1[i] < arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1

    # Add any remaining elements in arr1 or arr2 to the end
    sorted_list.extend(arr1[i:])
    sorted_list.extend(arr2[j:])
    return sorted_list


def merge_sort(arr):
    '''
    Recursive merge sort on an array or list of numbers.
    '''
    # Bottom of the recursion
    if len(arr) == 1:
        return arr

    # Recursively merge sort both halves
    arr1 = merge_sort(arr[:len(arr) // 2])
    arr2 = merge_sort(arr[len(arr) // 2:])

    # Merge the 2 sorted halves
    sorted_arr = merge(arr1, arr2)
    return sorted_arr

rng = np.random.default_rng()
#  arr = rng.integers(1, 1001, size=1000)
#  sorted_arr = merge_sort(arr)
#  print(sorted_arr)


#  lengths, times = time_sort(merge_sort,
                           #  lengths=[1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000],
                           #  repeat=5)

#  # Plot the results
#  fig, ax = plt.subplots()
#  ax.plot(lengths, times, 'kx')
#  ax.set_xlabel('Array size')
#  ax.set_ylabel('Execution time (s)')
#  plt.show()



# Quicksort
def quicksort(arr):
    '''
    Quicksort algorithm to sort elements of a list arr.
    '''
    # Terminating case: only one element left
    n = len(arr)
    if n <= 1:
        return arr

    # Find the pivot
    if pivot_type == 'random':
        pivot = arr[int(n * random.random())]
    elif pivot_type == 'median':
        mid = n // 2
        pivot = bubble_sort([arr[0], arr[mid], arr[-1]])[1]

    # Partition
    above = [i for i in arr if i > pivot]
    below = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]

    return quicksort(below) + equal + quicksort(above)

# Compare quicksort and mergesort
fig, ax = plt.subplots()
ax.set_xlabel('Array size')
ax.set_ylabel('Execution time (s)')

lengths, times = time_sort(merge_sort,
                           lengths=[1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000],
                           repeat=5)
ax.plot(lengths, times, 'kx', label='Merge sort')

pivot_type = 'random'
lengths, times = time_sort(quicksort,
                           lengths=[1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000],
                           repeat=5)
ax.plot(lengths, times, 'rx', label='Quick sort, random pivot')

pivot_type = 'median'
lengths, times = time_sort(quicksort,
                           lengths=[1000, 2000, 5000, 10000, 20000, 30000, 40000, 50000],
                           repeat=5)
ax.plot(lengths, times, 'bx', label='Quick sort, median-of-3 pivot')

ax.legend()
plt.show()
