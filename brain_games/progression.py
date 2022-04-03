#!/usr/bin/env python

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


# generate of a arithmetic progression-----------------------------------
def generate_arith_progression():
    global r
    while True:
        x = randint(0, 99)
        y = randint(0, 99)
        step = randint(1, 99)
        i = randint(5, 10)
        if x < y and step <= ((y - x) // 5):
            r = range(x, y, step)
            r = r[0:i]
            return r
        if y < x and step <= ((x - y) // 5):
            r = range(y, x, step)
            r = r[0:i]
            return r


# getting of the arithmetic progresson with a hidden char----------------
def get_sequence_with_hidden():
    global r, sequence_with_hidden, n
    generate_arith_progression()
    max_of_sequence = len(r) - 1
    n = randint(0, max_of_sequence)
    sequence_with_hidden = ''
    for i in r:
        if i == r[n]:
            i = '..'
        sequence_with_hidden += str(i) + ' '
    print(f"Question: {sequence_with_hidden}")


# execution of the correct answer from user-----------------------------
def execute_correct_answer():
    global answer, r, n, break_out_flag, s
    break_out_flag = False
    if answer == str(r[n]):
        print('Correct!')
        break_out_flag = True
        s += 1
    return break_out_flag


# execution of the wrong answer from user-------------------------------
def execute_wrong_answer():
    global answer, r, n
    if answer != str(r[n]):
        print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{str(r[n])}'.")
        return print("Let's try again, {}!".format(name))


# brain-gcd game function----------------------------------------------
def get_progression():
    global answer, name, break_out_flag, s
    name = welcome_user()
    s = 0
    print('What number is missing in the progression?')
    for i in range(3):
        generate_arith_progression()
        get_sequence_with_hidden()
        get_answer()
        execute_correct_answer()
        if break_out_flag is False:
            execute_wrong_answer()
            break
    if s == 3:
        print('Congratulations, {}!'.format(name))
