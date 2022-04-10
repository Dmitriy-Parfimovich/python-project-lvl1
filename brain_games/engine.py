#!/usr/bin/env python

import prompt


# the MAIN engine (function)
def main_engine(get_question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    iteration = 0
    for i in range(3):
        [rules, question, correct_value] = get_question()
        answer = ''
        if i == 0:
            print(rules)
        print('Question:', question)
        while answer == '':
            print('Your answer: ', end='')
            answer = input()
        if answer == str(correct_value):
            print('Correct!')
            iteration += 1
        if answer != str(correct_value):
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_value}'.")
            print("Let's try again, {}!".format(name))
            return
        if iteration == 3:
            print('Congratulations, {}!'.format(name))
