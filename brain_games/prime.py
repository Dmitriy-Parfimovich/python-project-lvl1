#!/usr/bin/env python

from brain_games.cli import welcome_user
from random import randint


# getting an answer from user-------------------------------------------
def get_answer():
    global answer, x
    x = randint(1, 99)
    answer = ''
    print('Question:', x)
    while answer == '' or (answer != 'yes' and answer != 'no'):
        print('Your answer: ', end='')
        answer = input()
    return answer, x


# checking of the prime number------------------------------------------
def check_prime_number():
    global x
    d = 2
    while d * d <= x and x % d != 0:
        d += 1
    return d * d > x


# execution of the correct answer from user-----------------------------
def execute_correct_answer():
    global answer, x, break_out_flag, s
    break_out_flag = False
    if answer == 'yes' and check_prime_number() == True:
        print('Correct!')
        break_out_flag = True
        s += 1
    if answer == 'no' and check_prime_number() == False:
        print('Correct!')
        break_out_flag = True
        s += 1


# execution of the wrong answer from user-------------------------------
def execute_wrong_answer():
    global answer, x
    if answer == 'yes' and check_prime_number() == False:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return print("Let's try again, {}!".format(name))
    if answer == 'no' and check_prime_number() == True:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return print("Let's try again, {}!".format(name))


# brain-even game function----------------------------------------------
def get_prime():
    global answer, x, name, break_out_flag, s
    name = welcome_user()
    s = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        get_answer()
        execute_correct_answer()
        if break_out_flag is False:
            execute_wrong_answer()
            break
    if s == 3:
        print('Congratulations, {}!'.format(name))
