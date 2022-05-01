#!/usr/bin/env python

from random import randint, choice


# constants and the rules of the brain-calc game
START_VALUE1 = 0
START_VALUE2 = 0
FINAL_VALUE1 = 99
FINAL_VALUE2 = 99
RULES = 'What is the result of the expression?'


# the calc function question and answer calculation
def get_question():
    random_num1 = randint(START_VALUE1, FINAL_VALUE1)
    random_num2 = randint(START_VALUE2, FINAL_VALUE2)
    arithmetic = ['+', '-', '*']
    arithmetic = choice(arithmetic)
    question = (f"{str(random_num1)} {arithmetic} {str(random_num2)}")
    if arithmetic == '+':
        correct_value = random_num1 + random_num2
    if arithmetic == '-':
        correct_value = random_num1 - random_num2
    if arithmetic == '*':
        correct_value = random_num1 * random_num2
    return question, correct_value
