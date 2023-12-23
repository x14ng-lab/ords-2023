## Exercise 1

```python
# Define the function
def seq_Perrin():
    '''
    Yields elements of the sequence of Perrin numbers.
    '''
    c = 3
    yield c    # first stopping point
    
    b, c = c, 0
    yield c    # second stopping point
    
    a, b, c = b, c, 2
    yield c    # third stopping point
    
    while True:
        a, b, c = b, c, a+b
        yield c    # all the subsequent stopping points

# Create the generator
gen_Perrin = seq_Perrin()

# Use the generator
for i in range(16):
    print(next(gen_Perrin))
```

---

## Exercise 2

```python
ger = oil_data.loc[:, 'Germany'] < 20000
bel = oil_data.loc[:, 'Belgium'] > 4000
print(oil_data.loc[ger & bel, 'Denmark'])
```

---

## Exercise 3

```python
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

# Read in our data
randd = pd.read_csv('r_and_d_spend.csv')
print(randd)

# Plot the data for all countries
fig, ax = plt.subplots(2, 4, figsize=(12, 6))
i = 0
j = 0
nb_plots = 7
plot_index = 0

while plot_index < nb_plots:
    country = randd.columns[plot_index + 1]
    
    # Plot the data points
    ax[i, j].plot(randd['Year'], randd[country], 'ko', label=country)
    
    # Linear regression
    reg = st.linregress(randd['Year'], randd[country])
    line = randd['Year'] * reg.slope + reg.intercept
    
    ax[i, j].plot(randd['Year'], line, 'r-', label='Linear fit')
    
    # Axes properties
    ax[i, j].legend(loc='upper left')
    if i == 1:
        ax[i, j].set_xlabel('Year')
    if j == 0:
        ax[i, j].set_ylabel('% of GDP')

    plot_index += 1
    j += 1
    # Move to the next row
    if j > 3:
        j = 0
        i += 1

ax[1, 3].axis('off')
plt.show()
```

---

## Exercise 4

```python
fig, ax = plt.subplots(figsize=(9, 6))

years = (randd['Year'] >= 2000) & (randd['Year'] <= 2010)
country = randd.columns[1:]
colours = plt.cm.get_cmap('rainbow')

for i in range(7):
    ax.plot(randd.loc[years, 'Year'], randd.loc[years, country[i]], 'o', color=colours(i/7), label=country[i])

ax.set_title('R & D spend in % of GDP')
ax.set_xlabel('Year')
ax.set_ylabel('% of GDP')
ax.set_ylim([0, 4])
ax.legend(loc='upper left')
plt.show()
```
