## Exercise 1

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

# Store y-axis label for each plot
y_labels = [r'$f_1(x)$', r'$f_2(x)$', r'$f_3(x)$']

# Set all 3 properties for the 3 plots
for i in range(3):
    ax[i].set_xlim([-np.pi, np.pi])
    ax[i].set_xlabel(r'$x$', fontsize=14)
    ax[i].set_ylabel(y_labels[i], fontsize=14)

# Make some space
plt.subplots_adjust(hspace=0.5, wspace=0.5)

# Display the plot
plt.show()
```

---

## Exercise 2

```python
import matplotlib.pyplot as plt
import numpy as np
import math

# Define a function for the truncated Maclaurin series
def trunc_cos(x, n):
    '''
    Return the truncated Maclaurin series for
    cos(x), with terms up until order n.
    '''
    cos_series = 0
    for k in range(n//2 + 1):
        # Add each term of the series up to nth order
        cos_series += (-1)**k * x**(2*k) / math.factorial(2*k)
    
    return cos_series


# Create an x-axis with 1000 points
x = np.linspace(-np.pi, np.pi, 1000)

# Create a figure
fig, ax = plt.subplots()

# Plot the requested functions
ax.plot(x, np.cos(x), 'k-', label=r'$\cos(x)$')
ax.plot(x, trunc_cos(x, 2), 'r--', label=r'Order 2')
ax.plot(x, trunc_cos(x, 4), 'g-.', label=r'Order 4')
ax.plot(x, trunc_cos(x, 6), 'b:', label=r'Order 6')

# Set axis properties
ax.set_xlim([-np.pi, np.pi])
ax.set_ylim([-1.5, 1.5])
ax.set_xlabel(r'$x$', fontsize=12)
ax.legend()

plt.show()
```

---

## Exercise 3

```python
import matplotlib.pyplot as plt
import numpy as np

# Let's write a convenience function
def f(x):
    # Set coefficients
    a, b, c = -1, 3, 5
    
    # Compute the roots
    sqrt_delta = np.sqrt(b**2 - 4*a*c)
    roots = [(-b - sqrt_delta)/(2 * a), (-b + sqrt_delta)/(2 * a)]
    
    # Return the polynomial and the 2 roots
    return a*x**2 + b*x + c, roots

# Create an x-axis, compute f(x) and both roots
x = np.linspace(-4, 5, 100)
y, roots = f(x)

# Create the figure and axes
fig, ax = plt.subplots(1, 1, figsize=(9, 5))

# Plot the function and the roots
ax.plot(x, y, '--', color='deepskyblue', label=r'$f(x) = -x^2 + 3x + 5$')
ax.plot(x, np.zeros(x.shape[0]), 'k-', label=r'$y = 0$')
ax.plot(roots[0], 0, 'magenta', label='First root', marker='^', markersize=10)
ax.plot(roots[1], 0, 'magenta', label='Second root', marker='^', markersize=10)

# Tidy up the plot
ax.set_xlim([-4, 5])
ax.set_ylim([y[0], 10])
ax.set_xticks(range(-4, 6))
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title('Polynomial roots', fontsize=14)
ax.legend(loc='lower center')
ax.grid(True)

plt.show()
```

---

## Exercise 4

```python
import random

def random_letters(word, number_of_letters):
    '''
    Returns a list of number_of_letters randomly selected letters
    from a given word.

    Input:
        word (str): a string of characters representing a word
        number_of_letters (int): an integer representing the total
            number of random letters we want to return

    Output:
        list_of_letters (list): a list of number_of_letters random letters
            from the input word.
    '''
    list_of_letters = []

    for i in range(number_of_letters):
        index = random.randint(0, len(word)-1)
        letter = word[index]
        list_of_letters.append(letter)

    return list_of_letters
```

---

## Exercise 5

```python
# Statistics for Bulgaria
mode, count = stats.mode(bulgaria)
print('Bulgaria:\n',
      f'Median = {np.median(bulgaria):.1f}\n',
      f'Mode = {mode[0]:.1f}, appearing {count[0]:d} times ({100*count[0]/len(bulgaria):.1f}% of the time)\n',
      f'Geometric mean = {stats.gmean(bulgaria):.2f}\n')

# For example, calculate the Pearson correlation coefficient
# between all pairs of countries
countries = ['Germany', 'Denmark', 'Belgium', 'Bulgaria']

pearson_coeffs = []

for country1 in oil_data.T:
    country1_coeffs = []
    for country2 in oil_data.T:
        # The coefficient is the first output of stats.pearsonr
        country1_coeffs.append(np.round(stats.pearsonr(country1, country2)[0], 2))
    
    # Add all coeffs with country1 to the main array
    pearson_coeffs.append(country1_coeffs)

# Display the results in a table, highlight correlated columns
colourmap = plt.cm.get_cmap('Greens')   # get a colourmap function to map colours to numbers
colours = colourmap(pearson_coeffs)

fig, ax = plt.subplots(1, 1, figsize=(7, 2))
ax.table(cellText=pearson_coeffs,
         rowLabels=countries,
         colLabels=countries,
         cellColours=colours,
         loc='center',
         cellLoc='center')
ax.axis('tight')
ax.axis('off')
plt.show()

# Germany and Denmark seem correlated, let's try to find a linear relationship
fig, ax = plt.subplots(1, 1, figsize=(7, 5))
ax.plot(germany, denmark, 'kx', label='Data points')
ax.set_xlabel('Oil reserves for Germany')
ax.set_ylabel('Oil reserves for Denmark')

# We can create a linear regression object using stats.linregress
regr = stats.linregress(germany, denmark)

# Then we plot the line on the same graph
x_values = np.arange(germany.min(), germany.max(), 100)
y_values = x_values * regr.slope + regr.intercept
ax.plot(x_values, y_values, 'r-', label=f'Linear fit (R^2 = {regr.rvalue**2:.2f})')

ax.legend()
plt.show()
```

---

## Exercise 6

The objective function to minimise now gives the number of work hours in a week, given by $f(x_T, x_C) = 6x_T + 3x_C$. Constraint 1 is removed, and a new constraint is the minimum profit:
$$
30x_T + 10x_C \geq 150.
$$

Constraint 3 becomes, with the new available storage space:
$$
x_C/4 + x_T \leq 8.
$$

If we add the extra constraint on the number of chairs and tables, constraint 2 is replaced by an equality:
$$
x_C = 3x_T.
$$

```python
from scipy.optimize import linprog

# A still must be a matrix (here, with a single row)
A = np.array([[-30, -10],
              [1, 0.25]], dtype=float)

b = np.array([-150, 8], dtype=float)
c = np.array([6, 3], dtype=float)

# We need to provide equality constraints separately
A_eq = np.array([[3, -1]], dtype=float)
b_eq = np.array([0], dtype=float)

solution = linprog(c, A, b, A_eq, b_eq)
results = A @ solution.x
print(f'The optimal strategy is to make {solution.x[0]:.2f} tables',
      f'and {solution.x[1]:.2f} chairs every week (on average), which',
      f'takes {solution.fun:.1f} hours per week.',
      f'The total profit is {-results[0]:.2f}.',
      f'The furniture takes up {100*results[1]/8:.1f}% of storage space.')
```

---
