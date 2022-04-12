#!/usr/bin/env python

from random import randint, choice


# the rules of the brain-calc game
rules = 'What is the result of the expression?'


# the calc function question and answer calculation
def get_question():
    RANDOM_NUM1 = randint(0, 99)
    RANDOM_NUM2 = randint(0, 99)
    arithmetic = ['+', '-', '*']
    arithmetic = choice(arithmetic)
    question = (f"{str(RANDOM_NUM1)} {arithmetic} {str(RANDOM_NUM2)}")
    if arithmetic == '+':
        correct_value = RANDOM_NUM1 + RANDOM_NUM2
    if arithmetic == '-':
        correct_value = RANDOM_NUM1 - RANDOM_NUM2
    if arithmetic == '*':
        correct_value = RANDOM_NUM1 * RANDOM_NUM2
    return question, correct_value
