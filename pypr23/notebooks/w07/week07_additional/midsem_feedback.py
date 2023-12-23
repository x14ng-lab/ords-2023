# Word cloud generation code:
# Adapted from 'wordcloud' documentation
# http://amueller.github.io/word_cloud/auto_examples/simple.html#sphx-glr-auto-examples-simple-py
# Accessed 30th October 2023.

from wordcloud import WordCloud
import string

# Open the data file and read the lines
with open('scrambled_midsem_feedback.csv', 'r') as f:
    responses = f.readlines()

question = 0
all_answers = []

# Collect all answers to one question in a list
for student in responses:
    answers = student.split(sep='\t')
    all_answers.append(answers[question])
    # print(len(answers))

# print(all_answers)
# print(responses)

# Concatenate all answers into one long string
# print(' SEPARATE '.join(['a', 'b', 'c', 'd']))
all_answers = ' '.join(all_answers).lower()
# all_answers = all_answers.lower()
# print(all_answers)

# Cleaning the text

# Removing punctuation
# (only keeping the characters we want)
# answer_words = ''
# for char in all_answers:
#     # if char in string.ascii_lowercase or char == ' ':
#     if char in string.ascii_lowercase + ' ':
#         answer_words = answer_words + char

# using a comprehension
answer_words = ''.join([char for char in all_answers if char in string.ascii_lowercase + ' '])


# Remove words that aren't useful
to_ignore = ['lecture', 'lectures', 'video', 'videos']


# print(answer_words)

# # Generate a word cloud image
wordcloud = WordCloud(width=800, height=600, background_color="white").generate(answer_words)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
