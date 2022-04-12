#!/usr/bin/env python

import prompt


# the MAIN engine (function)
def main_engine(get_question, rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rules)
    for i in range(3):
        [question, correct_value] = get_question()
        answer = get_answer(question)
        get_game_variants(name, answer, correct_value)
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


# performing a correct answer
def get_game_variants(name, answer, correct_value):
    if answer == str(correct_value):
        print('Correct!')
