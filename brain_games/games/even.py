#!/usr/bin/env python

from random import randint


# the even function, question and answer calculation
def get_question():
    x = randint(0, 99)
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = str(x)
    if x % 2 == 0 and x != 0:
        correct_value = 'yes'
    if x % 2 != 0 or x == 0:
        correct_value = 'no'
    return rules, question, correct_value
