#!/usr/bin/env python

from brain_games.cli import welcome_user
from random import randint, choice


# getting an answer from user-------------------------------------------
def get_answer():
    global answer, calc
    x = randint(0, 99)
    y = randint(0, 99)
    arithmetic = ['+', '-', '*']
    arithmetic = choice(arithmetic)
    answer = ''
    print(f"Question: {x} {arithmetic} {y}")
    if arithmetic == '+':
        calc = x + y
    if arithmetic == '-':
        calc = x - y
    if arithmetic == '*':
        calc = x * y
    while answer == '':
        print('Your answer: ', end='')
        answer = input()
    return answer, calc


# execution of the correct answer from user-----------------------------
def execute_correct_answer():
    global answer, calc, break_out_flag, s
    break_out_flag = False
    if answer == str(calc):
        print('Correct!')
        break_out_flag = True
        s += 1
    return break_out_flag


# execution of the wrong answer from user-------------------------------
def execute_wrong_answer():
    global answer, calc
    if answer != str(calc):
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{calc}'.")
        return print("Let's try again, {}!".format(name))


# brain-calc game function----------------------------------------------
def get_calc():
    global answer, calc, name, break_out_flag, s
    name = welcome_user()
    s = 0
    print('What is the result of the expression?')
    for i in range(3):
        get_answer()
        execute_correct_answer()
        if break_out_flag is False:
            execute_wrong_answer()
            break
    if s == 3:
        print('Congratulations, {}!'.format(name))
