#!/usr/bin/env python

from random import randint


# the prime function, question and answer calculation
def get_question():
    x = randint(1, 99)
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = (str(x))
    divider = 2
    while divider * divider <= x and x % divider != 0:
        divider += 1
    if divider * divider > x:
        correct_value = 'yes'
    else:
        correct_value = 'no'
    return rules, question, correct_value
