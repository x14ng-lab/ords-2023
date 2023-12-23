## Exercise 1

```python
import random

n = 10
random_ints = []
for i in range(n):
    random_ints.append(random.randint(1, 10))

# Initialise a variable to hold the sum
total = 0

# Loop over the list of random ints
for number in random_ints:
    # Check if multiple of 3
    if number % 3 == 0:
        # Add it to the total
        total += number

# Display the result
print(f'The sum of all numbers in {random_ints} which are multiples of 3 is {total}.')
```


---

## Exercise 2

```python
import numpy as np

rng = np.random.default_rng()
n = rng.integers(1, 1001)

if n % 21 == 0:
    # if n is a multiple of 3x7, it's a multiple of both 3 and 7
    print(n, 'is a multiple of both 3 and 7.')
elif n % 3 == 0 or n % 7 == 0:
    # not a multiple of both, but a multiple of either
    print(n, 'is a multiple of one of 3 or 7.')
else:
    # the last possible case: not a multiple of either
    print(n, 'is not a multiple of 3 nor 7.')
```


---

## Exercise 3

```python
zen = 'If the implementation is hard to explain, it is a bad idea. If the implementation is easy to explain, it may be a good idea.'
count = 0

# The .split() method returns a list of words
for word in zen.split():
    if 'e' in word:
        print(word)
    elif 'i' in word:
        print(word[0])
    else:
        count += 1
```


---

## Exercise 4

```python
import math

e = 1
n = 0
while not math.isclose(math.exp(1), e, rel_tol=1e-6):
    n += 1                      # increment n by 1
    e += 1 / math.factorial(n)  # add the nth term of the series
    
    print(f'n = {n}')
    print(f'Exact value of exp(1): {math.exp(1):.6f}')
    print(f'Approximate value: {e:.6f}\n')

print(f'{n} iterations are needed.')
```


---

## Exercise 5

The outer loop runs for 10 iterations, and at each of these, the inner loop runs for 5 iterations. If the conditional `break` was absent, then we should see that `count` has reached $5\times 10 = 50$ after the loops: it is incremented 5 times each of the 10 iterations of the outer loop. The `print()` statement is inside the outer loop, but outside the inner loop: it executes only once per iteration of the outer loop, so we should see a total of 10 numbers displayed below the cell.

When `count` reaches 18, the **inner** loop breaks (but not the outer loop!). `count` is then printed, with the inner loop only having completed 3 iterations this time. We then start a new iteration of the outer loop, and enter the inner loop again (with `j` set to `0`), where `count` is incremented by 1 (so now `count` is `19`). Since `count > 17` is still `True`, we break the inner loop again (after just 1 iteration), `print(count)`, and start the new iteration of the outer loop. This continues until we've completed the 10 iterations of the outer loop.

`break` only breaks the **innermost** loop.

```python
count = 0

for i in range(10):
    for j in range(5):
        count += 1
        if count > 17:
            break   # this break...
    # ... leads us exactly here (just outside of the inner loop)
    print(count)
```

---

## Exercise 6

```python
def find_divisors(nums, n):
    '''
    Returns a list of all divisors of n
    present in the list nums.
    '''
    divisors = []
    for i in nums:
        
        print(f'Current number being tested is {i}.')
        print(f'Is {i} a divisor of {n}?')
        
        # Check if n/i is an integer number, instead of an 'int' object
        if n % i == 0:
            print(f'Yes, adding {i} to the list (oops, not n!)\n')
            divisors.append(i)
        else:
            print('No\n')
    
    return divisors

# Test example: result should be [1, 1, 1, 1] (no matter the choice of n)
divisors = find_divisors([1, 1, 1, 1], 97)
print(f'Result: {divisors}\n')

# Test example: result should be [1, 2, 3, 4, 6]
divisors = find_divisors([1, 2, 3, 4, 5, 6, 7, 8], 12)
print(f'Result: {divisors}\n')

# Test example: result should be [] for any number n smaller than all the list elements
divisors = find_divisors([10, 10, 10], 5)
print(f'Result: {divisors}\n')

# Test example: result should be [] for any prime number n and any list not containing 1 or n
divisors = find_divisors([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 23)
print(f'Result: {divisors}\n')

# Test example: result should be [1] for any prime number n and any list containing 1 but not n
divisors = find_divisors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 17)
print(f'Result: {divisors}\n')

# Test example: result should be [1, n] for any prime number n and any list containing 1 and n
divisors = find_divisors([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11)
print(f'Result: {divisors}\n')
```

An even more robust version of the last 4 tests would be to generate lists of random integers with the required properties.


---

## Exercise 7

There are enough code comments here, but they are not very helpful -- instead of explaining what the code does, they simply describe each line, and they don't give more information than you could get by just reading the code. This is a bit better, for example:
```python
def fibonacci(n):
    '''
    Returns the Fibonacci sequence up to xn,
    starting with x0 = 1, x1 = 1, as a list.
    '''
    # Start a list x with the two initial values
    x = [1, 1]
    
    # The list will be [x0, x1, ..., xn], which is n+1 total elements.
    # Add the remaining n-1 elements with a loop
    for i in range(n-1):
        # The next element is the sum of the 2 previous elements
        x.append(x[i] + x[i+1])
    
    return x

# Compute and display the Fibonacci sequence up to the 6th term
print(fibonacci(5))
```


---

## Exercise 8

```python
import numpy as np

# Set polynomial coefficient values
a = 2
b = .5
c = -9

# Compute square root of discriminant
sqrt_delta = np.sqrt(b**2 - 4*a*c)

# Compute the roots
x1 = (-b - sqrt_delta) / (2*a)
x2 = (-b + sqrt_delta) / (2*a)

# Display the roots
print('First root: x1 =', x1)
print('Second root: x2 =', x2)

# Check the results
print('Is x1 correct?', a*x1**2 + b*x1 + c == 0)
print('Is x2 correct?', a*x2**2 + b*x2 + c == 0)
```

- The `import` statement was moved to the start of the code. Generally, all `import` statements would be together at the top of a script.
- `numpy` was shortened to `np` to reduce cluttering.
- Code comments were added to describe the main steps in plain English.
- Spacing around operators was corrected to follow PEP8 guidelines, to improve readability.
- To avoid repeating computations twice, the square root of the discriminant was pre-calculated and assigned to a variable once.
- `print()` was used to display relevant output, together with a few words for context. Note that several values were printed with only one use of the `print()` function, by listing them as input arguments separated by a comma. (For instance, try `print(a, b, c)`.)
- To check the results, comparison operators were used to create a Boolean value, which more directly indicates the expected result to the reader.


---

## Exercise 9

```python
import numpy as np

rng = np.random.default_rng()
target = rng.integers(1, 101)

# Take a first guess
number = int(input('Guess the number between 1 and 100: '))

# Continue guessing until we find the answer
while True:
    if number > target:
        number = int(input('Too big! Try again: '))
    elif number < target:
        number = int(input('Too small! Try again: '))
    else:
        # Found the number -- break the loop
        print(f'Congratulations! You guessed {target} correctly.')
        break
```
