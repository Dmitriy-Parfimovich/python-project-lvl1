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


def execute_correct_yes():
    global x
    if x % 2 == 0 and x != 0:
        print('Correct!')


def execute_correct_no():
    global x
    if x % 2 != 0 or x == 0:
        print('Correct!')


def find_even():
    global name
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        get_answer()
        if answer == 'yes':
            execute_correct_yes()
            if x % 2 != 0 or x == 0:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                return print("Let's try again, {}!".format(name))
        if answer == 'no':
            execute_correct_no()
            if x % 2 == 0 and x != 0:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                return print("Let's try again, {}!".format(name))
    print('Congratulations, {}!'.format(name))
