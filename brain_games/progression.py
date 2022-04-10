#!/usr/bin/env python

from random import randint


# the progression function, question and answer calculation
def get_question():
    rules = 'What number is missing in the progression?'
    while True:
        sequence = range(randint(0, 99), randint(0, 99), randint(1, 99))
        if 4 < len(sequence) < 11:
            max_of_sequence = len(sequence) - 1
            num = randint(0, max_of_sequence)
            question = ''
            for i in sequence:
                if i == sequence[num]:
                    i = '..'
                question += str(i) + ' '
            correct_value = sequence[num]
            return rules, question, correct_value
