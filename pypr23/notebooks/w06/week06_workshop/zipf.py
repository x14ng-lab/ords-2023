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
    pass


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
    pass


# Add your code below to use your functions...
