#!/usr/bin/env python

import prompt


# constants
CYCLE_COUNT = 3


# the MAIN engine (function)
def main_engine(get_question, rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rules)
    for i in range(CYCLE_COUNT):
        [question, correct_value] = get_question()
        answer = get_answer(question)
        if answer == str(correct_value):
            print('Correct!')
        if answer != str(correct_value):
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_value}'.")
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, {}!'.format(name))


# getting the answer from user
def get_answer(question):
    print('Question:', question)
    answer = ''
    print('Your answer: ', end='')
    answer = input()
    return answer
