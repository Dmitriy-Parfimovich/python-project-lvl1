#!/usr/bin/env python

from random import randint


# the rules of the brain-even game
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


# the even function, question and answer calculation
def get_question():
    RANDOM_NUM1 = randint(0, 99)
    question = str(RANDOM_NUM1)
    if RANDOM_NUM1 % 2 == 0 and RANDOM_NUM1 != 0:
        correct_value = 'yes'
    else:
        correct_value = 'no'
    return question, correct_value
