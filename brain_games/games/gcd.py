#!/usr/bin/env python

from random import randint


# the rules of the brain-gcd game
rules = 'Find the greatest common divisor of given numbers.'


# the gcd function, question and answer calculation
def get_question():
    RANDOM_NUM1 = randint(1, 99)
    RANDOM_NUM2 = randint(1, 99)
    question = (f"{RANDOM_NUM1} {RANDOM_NUM2}")
    while RANDOM_NUM1 != RANDOM_NUM2:
        if RANDOM_NUM1 > RANDOM_NUM2:
            RANDOM_NUM1 = RANDOM_NUM1 - RANDOM_NUM2
        if RANDOM_NUM2 > RANDOM_NUM1:
            RANDOM_NUM2 = RANDOM_NUM2 - RANDOM_NUM1
    correct_value = RANDOM_NUM1
    return question, correct_value
