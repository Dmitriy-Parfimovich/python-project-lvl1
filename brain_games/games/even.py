#!/usr/bin/env python

from random import randint


# constants and the rules of the brain-even game
START_VALUE = 0
FINAL_VALUE = 99
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


# the even function, question and answer calculation
def get_question():
    random_num = randint(START_VALUE, FINAL_VALUE)
    question = str(random_num)
    if random_num % 2 == 0 and random_num != 0:
        correct_value = 'yes'
    else:
        correct_value = 'no'
    return question, correct_value
