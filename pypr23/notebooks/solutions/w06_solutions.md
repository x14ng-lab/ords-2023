## Exercise 1

```python
grades = {'Alice': {'maths': 'A', 'english': 'C', 'music': 'B'},
          'Bob': {'maths': 'C', 'english': 'A', 'history': 'A'},
          'Charlie': {'physics': 'D', 'music': 'A', 'biology': 'A'}}

# Change Alice's maths grade to B
grades['Alice']['maths'] = 'B'

# Add a C in English for Charlie
grades['Charlie']['english'] = 'C'

# Add grades for Dara
grades['Dara'] = {'maths': 'B', 'history': 'D'}

print(grades)
```

For dictionaries, the same command can be used to change an existing item or to create a new key.

Here, we have nested dictionaries: for instance, `grades['Alice']` should give us the *value* in the dictionary `grades` which corresponds to the *key* `'Alice'` --- and that value is *another dictionary*. This means that we can simply index it by key, just like any other dictionary --- for instance, the value corresponding to the key `'maths'` in the dictionary `grades['Alice']` is accessed with `grades['Alice']['maths']`.

---

## Exercise 2

```python
grades_by_subject = {}
for student, all_grades in grades.items():
    for subject, grade in all_grades.items():
        if subject not in grades_by_subject:
            # Subject key doesn't exist yet, create it and add the current student
            grades_by_subject[subject] = {student: grade}
        else:
            # Subject exists, add a new entry to the (nested) value dict
            grades_by_subject[subject][student] = grade

print(grades_by_subject)
```

---

## Exercise 3

```python
factors6 = [n**2+3 for n in range(50, 101) if (n**2 + 3)%6 == 0]
print(factors6)
```

---

## Exercise 4

```python
combinations = [i + j + k for i in 'abc' for j in 'abc' for k in 'abc' if not i==j==k]
print(combinations)
```

---

## Exercise 5

```python
def fib_rec(p, q, n):
    '''
    Return the nth element of the (p,q)-Fibonacci sequence.
    
    Input:
        p (int), positive integer, first coefficient
        q (int), positive integer, second coefficient
        n (int), positive integer
        
    Output:
        Fn (int), the nth element of the sequence, defined by
        F(n) = pF(n-1) + qF(n-2).
    '''
    if n == 1 or n == 2:
        return 1
    else:
        return p*fib_rec(p, q, n-1) + q*fib_rec(p, q, n-2)

print(fib_rec(1, 1, 15))
print(fib_rec(6, 4, 10))
print(fib_rec(2, 1, 35))
```

---

## Exercise 6

```python
# We can redefine our function nearest_PO to also give us the distances
def nearest_PO(residents, POs, metric):
    '''
    Finds the closest post office to all residents.
    
    Input:
        residents (ndarray): array with "pop" rows and 2 columns,
            each row is the (x, y) coordinates of 1 resident.
        POs (ndarray): array with 2 columns, each row is the (x, y)
            coordinates of a post office.
        metric (str): 'manhattan' for Manhattan distance, 'euclid' for Euclidean distance.
    
    Output:
        closest (ndarray): index of the closest post office to each resident,
            in terms of Euclidean distance.
    '''
    if metric == 'manhattan':
        order = 1
    elif metric == 'euclid':
        order = 2
    else:
        print('Enter a valid metric!')
        return
    
    # Prepare a list of lists to store all distances
    distances = []
    
    # Loop over post offices
    for po in POs:
        dist_po = []
        # Loop over residents
        for res in residents:
            # Get the 2-norm of each vector between a resident and a PO
            dist_po.append(np.linalg.norm(res - po, ord=order))
        
        # Add the list of distances for all residents to that PO
        distances.append(dist_po)
    
    # Convert our list of lists to a NumPy array
    distances = np.array(distances).T
    
    # Return the index of the nearest PO, along each row of the array (find the min for each resident)
    closest = np.argmin(distances, axis=1)
    
    # Keep the distances
    pop = residents.shape[0]
    dist_closest = np.zeros(pop)
    for i in range(pop):
        dist_closest[i] = distances[i, closest[i]]
    
    return closest, dist_closest


def average_time(speed, pop):
    '''
    Plot average time to walk to the nearest PO as a function of number of POs.
    
    Input:
        speed (float): walking speed, km/h
        pop (int): population size for the simulation.
    Output: None
    '''
    av_time = np.zeros([30, 2])
    residents = make_residents(pop)
    
    # Loop over number of post offices
    for n in range(1, 31):
        POs = create_POs(n)

        # Get distances to nearest PO with both metrics
        _, dist1 = nearest_PO(residents, POs, 'manhattan')
        _, dist2 = nearest_PO(residents, POs, 'euclid')

        # Get average distance and time
        av_dist1 = np.mean(dist1)
        av_time[n-1, 0] = av_dist1 / speed
        av_dist2 = np.mean(dist2)
        av_time[n-1, 1] = av_dist2 / speed
    
    # Plot the results
    fig, ax = plt.subplots()
    ax.plot(range(1, 31), av_time[:, 0], '-', label='Manhattan distance')
    ax.plot(range(1, 31), av_time[:, 1], '-', label='Euclidean distance')
    ax.legend()
    ax.set_xlabel('Number of post offices')
    ax.set_ylabel('Average walking time (hrs)')
    plt.show()

# This takes a little while to run -- you can start with a smaller population
average_time(5, 1000)
```
