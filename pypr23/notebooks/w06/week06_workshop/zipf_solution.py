import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Task 1
def word_frequencies(word_list):
    '''
    Reads a list containing multiple words, and returns a dictionary
    indicating the number of times each word was found in the string.

    Ignore capitalisation (e.g. 'Hello', 'HELLO', and 'hello' count as the same word).

    Input: word_list (list): a list of multiple words (as strings)
    Output: word_freq (dict): a dictionary where keys are the words,
        and values are the corresponding number of times each word appears
        in word_list

    Example:
    >>> print(word_frequencies(['Hello', 'Bonjour', 'hellO', 'hi', 'bonjour', 'BONJOUR']))
    {'hello': 2, 'bonjour': 3, 'hi': 1}

    >>> print(word_frequencies(['Potato', 'Tomato', 'Tornado']))
    {'potato': 1, 'tomato': 1, 'tornado': 1}
    '''
    word_freq = {}
    for word in word_list:
        # Convert all to lowercase
        w = word.lower()
        if w not in word_freq:
            # Current word not already in dictionary, add it and start counting
            word_freq[w] = 1
        else:
            # Current word already in dictionary, increment the corresponding value
            word_freq[w] += 1

    return word_freq


def zipf_law(word_freq, n):
    '''
    Plots the log frequencies of the n most frequent words in the
    dictionary word_freq.

    Fits a line through the log-log data to find the exponent of Zipf's law.

    Input:
        word_freq (dict): a dictionary where keys are the words,
            and values are the corresponding number of times
            each word appears in some text
        n (int): the number of most frequent words to plot

    Output: s (float): the exponent in Zipf's law
    '''
    # Sort dictionary by decreasing value (this is a dictionary comprehension!)
    word_freq = {key: val for key, val in sorted(word_freq.items(), key=lambda x: x[1], reverse=True)}

    # Plot the rank vs. frequency of the first n items in the sorted dict
    fig, ax = plt.subplots(figsize=(12, 9))
    x_data = np.log(range(1,n+1))
    y_data = np.log(list(word_freq.values())[:n])
    ax.plot(x_data, y_data, 'rx')

    # Linear fit
    reg = stats.linregress(x_data, y_data)
    s = reg.slope

    # Plot the line of best fit
    ax.plot(x_data, s*x_data + reg.intercept, 'b-')
    plt.show()

    return -s

# Read the file
with open('alice_words.txt', 'r') as f:
    word_string = f.read()

# Make the dictionary, plot the results, find the slope of the line of best fit
word_freq = word_frequencies(word_string.split())
slope = zipf_law(word_freq, 100)
print(slope)


# Task 2
import string

def cleanup_text(filename, start, stop):
    '''
    Returns the words in the text of some filename, without whitespace
    or punctuation, in a list.

    Input:
        filename (str): name of a .txt file to read
        start, stop (int): index of first and last lines which counts as text
            (to exclude headers/footers in the file)

    Output:
        word_list (list): a list of all the words in the text, without whitespace
            or punctuation
    '''
    # Open the file, read the lines from start to stop
    with open(filename, 'r') as f:
        lines = f.readlines()[start:stop+1]

    # Start a word list, loop over all lines
    word_list = []
    for line in lines:
        # Split the line along spaces into multiple words
        words = line.split(' ')

        # Clean up each word
        for word in words:
            # See documentation for str.join(): https://docs.python.org/3/library/stdtypes.html#str.join
            # and for string.ascii_letters: https://docs.python.org/3/library/string.html#string.ascii_letters
            clean_word = ''.join(char for char in word if char in string.ascii_letters)
            if clean_word:
                # If there were any actual letters in the word, append it to the list
                word_list.append(clean_word)

    return word_list

# Analyse Dr Jekyll and Mr Hyde
word_list = cleanup_text('jekyll.txt', 60, 2583)
freqs = word_frequencies(word_list)
s = zipf_law(freqs, 100)
print(s)


#  # Uncomment to see examples of usage for str.join():
#  print('SEPARATOR'.join(['aaa', 'bbb', 'ccc']))
#  print(';'.join(['one', 'two', 'three']))
#  print(''.join(['Do', 'Re', 'Mi']))
#  print('\n'.join(['First line', 'Second line', 'Third line']))

#  # Uncomment to see examples of strings provided by the string module
#  import string
#  print(string.ascii_letters)
#  print(string.punctuation)
#  print(string.digits)

#  sentence = 'I have 3 siblings, including a 2-year-old sister.'

#  # Create a new string containing all characters except the white spaces
#  no_whitespace = ''.join(char for char in sentence if char not in string.whitespace)
#  print(no_whitespace)

#  # Create a new string containing only the numbers and the punctuation
#  numbers_and_punct = ''.join(char for char in sentence if char in string.punctuation + string.digits)
#  print(numbers_and_punct)

#  # Create a new string with all lowercase and no punctuation
#  lowercase = ''.join(char.lower() for char in sentence if char not in string.punctuation)
#  print(lowercase)
