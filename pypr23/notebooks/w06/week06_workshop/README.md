# Week 6 workshop: Zipf's law

In language studies, [Zipf's law](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176592/) is an observation which has been empirically verified in written corpuses in many different languages.

Let r be the **rank** of a given word in a language, meaning that the rth most common word in the language has rank r. For example, in any English text, the word "the" usually has rank r=1, as it's usually the most common word in the text; the word "of" typically has rank r=2, as it's usually the second most common word; etc.

Zipf's law states that the **frequency** of the rth most common word in a language (i.e. how often the word occurs in that language) is proportional to 1/(r^s), where s is usually close to 1.

Intuitively, this means that the most common word in a language is typically used about twice as often as the second most common word, three times as often as the third most common word, etc.

Today, we'll verify whether this law applies to the text of *Alice's Adventures in Wonderland* by Lewis Carroll.

## Task 1: Zipf's law for *Alice's Adventures in Wonderland*

The file `alice_words.txt` contains the text of *Alice's Adventures in Wonderland*, as a single line, with all the words separated by a single space, and without any punctuation.

### Compute word frequencies

In the file `zipf.py`, write a function `word_frequencies()` which takes a **list of words** as an input, and returns a **dictionary** where the keys are all the **unique** words in the list of words, and the values are the number of times that each word appears in the list.

The docstring is already in `zipf.py`.

### Plot rank vs. frequency (log scale)

Write a function `zipf_law()` which takes a dictionary of word frequencies (e.g. the output of your function `word_frequencies()`) and an integer `n` as inputs. The function should:
- plot log(r) (on the x-axis) versus log(f(r)) (on the y-axis), where f(r) is the frequency of the rth most common word (the total number of times it appeared in the text), for the `n` most common words.
- perform linear regression on the data, plot the line of best fit on top of the data points. The slope of the line will give you the (negative) value of s -- return this value.

The docstring is already written, as well as the first line of the function, which sorts the dictionary in order to put the most common words first. (To find out how it works, consult the documentation for [`sorted`](https://docs.python.org/3/howto/sorting.html) and [lambda expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions).)

### Analyse the text

Read the file `alice_words.txt` and split it into a list of words. Use your functions to plot the frequencies of the 100 most common words in the text (on a log-log scale).

If Zipf's law is verified, you should see that this log-log plot is linear with a downwards slope -- is that the case? What's the value of s?

## Task 2: Confirm Zipf's law for other texts

The text in `alice_words.txt` comes from [Project Gutenberg](https://www.gutenberg.org/browse/scores/top), a website which contains .txt files for many books for which the copyright has expired. Browse the most popular books there, download a few, and try to verify Zipf's law in different books.

Click on a title, then right-click on "Plain Text - UTF-8" and click "Save target as" or "Save file" to download the .txt file on your computer. Upload it to your Codespace, the same way you usually upload `CRx.py` files for testing in code review tasks. Make sure it's in the same folder as `zipf.py`.

First, you will need to do a little bit of pre-processing of each text file, to obtain a list of lowercase words for your functions to analyse. To do so, you could create a function `cleanup_text()` which takes an input .txt file, and returns such a list of words. Here is roughly how to proceed:

- Open the file in any text editor, and find the first and last lines of the actual text (i.e. excluding the information/metadata in the header and footer of the file). These line numbers could also be given as inputs to your function `cleanup_text()`.
- Then, use `open()` to read the text of the file between this first and last lines.
- Once you have the text as `str` object(s), split it into individual words (you can assume that words on the same line are separated by a space).
- For each word, remove any character that's not a letter. Put all the words in the whole text into a big list of words.

After that, you can use your previous functions to build the dictionary of word frequencies, plot the results, and find the slope of the line of best fit.

Some useful functions:

- [The `string` module](https://docs.python.org/3/library/string.html)
- [`str` methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
