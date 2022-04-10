#!/usr/bin/env python

from random import randint


# the gcd function, question and answer calculation
def get_question():
    x = randint(1, 99)
    y = randint(1, 99)
    rules = 'Find the greatest common divisor of given numbers.'
    question = (f"{x} {y}")
    while x != y:
        if x > y:
            x = x - y
        if y > x:
            y = y - x
    correct_value = x
    return rules, question, correct_value
