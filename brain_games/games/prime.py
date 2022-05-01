#!/usr/bin/env python

from random import randint


# constants and the rules of the brain-prime game
START_VALUE = 1
FINAL_VALUE = 99
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# the prime function, question and answer calculation
def get_question():
    random_number = randint(START_VALUE, FINAL_VALUE)
    question = (str(random_number))
    correct_value = ''
    correct_value = 'yes' if is_prime(random_number) else 'no'
    return question, correct_value


# determining if a number is prime
def is_prime(number):
    divider = 2
    while divider * divider <= number and number % divider != 0:
        divider += 1
    if divider * divider > number:
        return divider
