#!/usr/bin/env python

import prompt
from brain_games.cli import welcome_user
from random import randint


# getting an answer from user-------------------------------------------
def get_answer():
    global answer
    answer = ''
    while answer == '':
        print('Your answer: ', end='')
        answer = input()
    return answer


# calculation of the gcd------------------------------------------------
def calculation_gcd():
    global x, y
    print(f"Question: {x} {y}")
    while x != y:
        if x > y:
            x = x - y
        if y > x:
            y = y - x
    return x


# execution of the correct answer from user-----------------------------
def execute_correct_answer():
    global x, answer, break_out_flag, iteration
    break_out_flag = False
    if answer == str(x):
        print('Correct!')
        break_out_flag = True
        iteration += 1
    return break_out_flag


# execution of the wrong answer from user-------------------------------
def execute_wrong_answer():
    global x, answer
    if answer != str(x):
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{x}'.")
        return print("Let's try again, {}!".format(name))


# brain-gcd game function (MAIN)-----------------------------------------
def get_gcd():
    global x, y, answer, name, break_out_flag, iteration
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have you name? ')
    print('Hello, {}!'.format(name))
    iteration = 0
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        x = randint(1, 99)
        y = randint(1, 99)
        calculation_gcd()
        get_answer()
        execute_correct_answer()
        if break_out_flag is False:
            execute_wrong_answer()
            break
    if iteration == 3:
        print('Congratulations, {}!'.format(name))
