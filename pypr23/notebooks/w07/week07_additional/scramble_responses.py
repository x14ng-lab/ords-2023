import numpy as np

with open('midsem_feedback.csv', 'r') as f:
    responses = f.readlines()


##

by_question = []

for question in range(6):

    all_answers = []

    for student in responses:
        answers = student.split(sep='\t')
        words = ''.join([char for char in answers[question] if char not in ['"', '\n']]).split(' ')
        all_answers += words

    scrambler = list(range(len(all_answers)))
    np.random.shuffle(scrambler)

    all_answers = list(np.array(all_answers)[scrambler])
    by_question.append(all_answers)


##

N_responses = min([len(q) for q in by_question]) // 10
all_new_answers = []

for q in by_question:

    new_answers = []
    words_per_response = len(q) // N_responses

    for word_index in range(N_responses):
        new_answers.append(q[words_per_response*word_index:words_per_response*(word_index + 1)])

    new_answers.append(q[words_per_response*word_index:])
    all_new_answers.append(new_answers)


##

new_text = ''

for r_index in range(N_responses):

    new_text_answer = ''

    for q_index in range(6):
        new_text_answer += '"' + ' '.join(all_new_answers[q_index][r_index]) + '"\t'

    new_text += new_text_answer + '\n'


##

with open('scrambled_midsem_feedback.csv', 'w') as f:
    f.write(new_text)
