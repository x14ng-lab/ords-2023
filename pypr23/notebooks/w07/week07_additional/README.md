# Python Programming - Week 7 lecture

Code for the Week 7 video and lecture.


## Lecture follow-up practice questions

I've added the file `scrambled_midsem_feedback.csv`, which contains a scrambled version of your responses to the mid-semester feedback survey. This preserves privacy of individual responses, but in particular should generate exactly the same word clouds.

You can use [this link to create your own repository for this lecture and work on the code](https://classroom.github.com/a/rz1wS52C).

Here are some suggested questions to work on, if you'd like more practice problems this week:

- The script I've used to create the scrambled data is `scramble_responses.py`. I haven't written any code comments. Study it carefully, and try to understand exactly how it works. (This is good practice for [_program comprehension_](https://static.teachcomputing.org/pedagogy/QR14-Code-tracing.pdf)!)
- Continue adding the functionality at the end of the script to remove certain words from the word cloud.
    - You will need a list of the words you want to ignore.
    - You will need to split the big string of text into words, and remove any words that are also in your 'ignore' list (or, as we saw in the lecture, keep all words that are _not_ in your 'ignore' list).
- Refactor the code into a function, which takes as arguments a file name where the data is located, a question index (between 0 and 5), a list of words you want to ignore.
- The `wordcloud` package, as we saw in the lecture, automatically ignores a default set of stopwords. Modify the code to make it ignore any word from [this list](https://github.com/stopwords-iso/stopwords-en/blob/master/stopwords-en.txt) instead. (You can download the `stopwords-en.txt` file from the link by clicking the "Download raw file" button on the top right.)
- Write a function which creates and displays a figure with 6 subplots, each containing the word cloud for 1 question. Each word cloud should be labelled to indicate which question the answers correspond to. As a reminder the 6 questions were (in order):
    1. Lectures/videos positives
    2. Lectures/videos negatives
    3. Notebook positives
    4. Notebook negatives
    5. Workshop positives
    6. Workshop negatives
