#!/usr/bin/env python

from random import randint


# constants and the rules of the brain-gcd game
START_VALUE1 = 1
START_VALUE2 = 1
FINAL_VALUE1 = 99
FINAL_VALUE2 = 99
rules = 'Find the greatest common divisor of given numbers.'


# the gcd function, question and answer calculation
def get_question():
    random_num1 = randint(START_VALUE1, FINAL_VALUE1)
    random_num2 = randint(START_VALUE2, FINAL_VALUE2)
    question = (f"{random_num1} {random_num2}")
    correct_value = get_gcd(random_num1, random_num2)
    return question, correct_value


# determining of gcd between two numbers
def get_gcd(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        if number_2 > number_1:
            number_2 = number_2 - number_1
    gcd = number_1
    return gcd
