#!/usr/bin/env python

from brain_games.cli import welcome_user
from random import randint


def get_answer():
    global answer, x
    x = randint(0, 99)
    answer = ''
    print('Question:', x)
    while answer == '' or (answer != 'yes' and answer != 'no'):
        print('Your answer: ', end='')
        answer = input()
    return answer, x


def execute_correct_answer():
    global answer, x, break_out_flag, s
    break_out_flag = False
    if answer == 'yes' and x % 2 == 0 and x != 0:
        print('Correct!')
        break_out_flag = True
        s += 1
    if answer == 'no' and (x % 2 != 0 or x == 0):
        print('Correct!')
        break_out_flag = True
        s += 1


def execute_wrong_answer():
    global answer, x
    if answer == 'yes' and (x % 2 != 0 or x == 0):
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return print("Let's try again, {}!".format(name))
    if answer == 'no' and x % 2 == 0 and x != 0:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return print("Let's try again, {}!".format(name))


def find_even():
    global answer, x, name, break_out_flag, s
    name = welcome_user()
    s = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        get_answer()
        execute_correct_answer()
        if break_out_flag is False:
            execute_wrong_answer()
            break
    if s == 3:
        print('Congratulations, {}!'.format(name))
