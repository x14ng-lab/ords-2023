## Exercise 1

```python
import numpy as np

# Create the matrix M
M = np.array([[9, 3, 0], [-2, -2, 1], [0, -1, 1]])

# Create the vector y
y = np.array([0.4, -3, -0.3])
```

---

## Exercise 2

```python
import numpy as np

def dot_prod(u, v):
    '''
    Returns the dot product of vectors u and v.
    '''
    return np.sum(u * v)
```

---

## Exercise 3

```python
# Create a random number generator
rng = np.random.default_rng()

# Create a random 3x5 matrix of integers between 1 and 10
A = rng.integers(1, 11, size=[3, 5])
print(A, '\n')

# Create a Boolean array the same shape as A, with True where the corresponding
# elements of A are smaller than 5, and False elsewhere
A5 = A < 5
print(A5, '\n')

# Use A5 to return all elements of A smaller than 5 (in a 1D array)
print(A[A5], '\n')

# Display the rows of A starting at row 1, and columns ending at column 2
print(A[1:, :3], '\n')

# Display the elements of that sub-matrix which are smaller than 5
print(A[1:, :3][A5[1:, :3]], '\n')

# Reassign all elements of A which are greater than or equal to 5 with the value 100
A[np.logical_not(A5)] = 100
print(A)
```

This is an example of how you can use **Boolean indexing** to extract elements of an array which fulfill certain conditions.

---

## Exercise 4

```python
n = 4

# Initialise A with zeros
A = np.zeros([n, n])

# Loop over the rows...
for i in range(n):
    # Loop over the columns...
    for j in range(n):
        if i < j:
            A[i, j] = i + 2*j
        else:
            A[i, j] = i * j

print(A)
```

---

## Exercise 5

```python
import numpy as np

# Create a random number generator
rng = np.random.default_rng()

# Create a random matrix A with 2000x2000 elements between -1 and 1.05
n = 2000
A = (1.05 + 1) * rng.random([n, n]) - 1.

# Get the sum of all rows of A
row_sums = np.sum(A, axis=1)

# Display the proportion of rows with a positive sum
positive_sum_rows = np.sum(row_sums >= 0)
print(f'The probability that a row of A is positive',
      f'is approximately {100 * positive_sum_rows / n : .1f}%.')
```

---

## Exercise 6

```python
# Assuming we still have M and y in memory from Exercise 1...
x = np.linalg.solve(M, y)
print(f'x = {x}')

# Print the norms
print(f'The 2-norm of x is {np.linalg.norm(x, 2)}.')
print(f'The infinity-norm of x is {np.linalg.norm(x, np.inf)}.')
```

---

## Exercise 7

```python
# Create an x-axis with 1000 points
x = np.linspace(-np.pi, np.pi, 1000)

# Evaluate the functions at all these points
f1 = np.sin(x)
f2 = np.tan(0.49 * x)
f3 = np.sin(x) * np.cos(2*x)

# Create the plots in the same axes
plt.plot(x, f1, 'r-.')
plt.plot(x, f2, 'g:')
plt.plot(x, f3, 'b--')

# Display the plot
plt.show()
```

---

## Exercise 8

```python
import matplotlib.pyplot as plt
import numpy as np

# Create an x-axis with 1000 points
x = np.linspace(-np.pi, np.pi, 1000)

# Evaluate the functions at all these points
f1 = np.sin(x)
f2 = np.tan(0.49 * x)
f3 = np.sin(x) * np.cos(2*x)

# Create a figure with 3 subplots
fig, ax = plt.subplots(1, 3, figsize=(10, 4))

# Plot each function in a different subplot
ax[0].plot(x, f1, 'r-.')
ax[1].plot(x, f2, 'g:')
ax[2].plot(x, f3, 'b--')

# Display the plot
plt.show()
```

---

## Exercise 9

```python
# first approach: using 'readline'
with open('mytextfile.txt','r') as myfile:
    # Initialise an empty list to store the lines
    all_lines = []

    # if line is empty, the end of file is reached 
    while True:
        # use readline to read the next line
        line = myfile.readline()

        # Break the loop when we reach an empty line (remember Boolean casting!)
        if not line:
            break

        # Append to the list if we still have non-empty lines
        all_lines.append(line)

# second approach: using 'readlines'
with open('mytextfile.txt','r') as myfile:
    all_lines = myfile.readlines()
    
print(all_lines)
```

---

## Exercise 10

```python
# Read the file, store the lines in a list
with open('mytextfile.txt', 'r') as myfile:
    all_lines = myfile.readlines()
    
# Edit and write each new line to a new file
with open('textfile_linenumber.txt', 'w') as newfile:
    count = 1
    for line in all_lines:
        newfile.write(f'{count}: {line}')
        count += 1
```
