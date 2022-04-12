#!/usr/bin/env python

from random import randint


# the rules of the brain-prime game
rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# the prime function, question and answer calculation
def get_question():
    RANDOM_NUM1 = randint(1, 99)
    question = (str(RANDOM_NUM1))
    correct_value = ''
    correct_value = 'yes' if is_prime(RANDOM_NUM1) else 'no'
    return question, correct_value


# determining if a number is prime
def is_prime(RANDOM_NUM1):
    divider = 2
    while divider * divider <= RANDOM_NUM1 and RANDOM_NUM1 % divider != 0:
        divider += 1
    if divider * divider > RANDOM_NUM1:
        return True
    else:
        return False
