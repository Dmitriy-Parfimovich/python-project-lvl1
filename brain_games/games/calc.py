#!/usr/bin/env python

from random import randint, choice


# the calc function question and answer calculation
def get_question():
    x = randint(0, 99)
    y = randint(0, 99)
    arithmetic = ['+', '-', '*']
    arithmetic = choice(arithmetic)
    rules = 'What is the result of the expression?'
    question = (f"{str(x)} {arithmetic} {str(y)}")
    if arithmetic == '+':
        correct_value = x + y
    if arithmetic == '-':
        correct_value = x - y
    if arithmetic == '*':
        correct_value = x * y
    return rules, question, correct_value
