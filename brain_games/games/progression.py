#!/usr/bin/env python

from random import randint


# constants and the rules of the brain-progression game
START_VALUE = 0
FINAL_VALUE = 99
START_STEP = 1
FINAL_STEP = 20
MIN_LENGTH = 5
MAX_LENGTH = 10
rules = 'What number is missing in the progression?'


# the progression function, question and answer calculation
def get_question():
    start = randint(START_VALUE, FINAL_VALUE)
    step = randint(START_STEP, FINAL_STEP)
    length = randint(MIN_LENGTH, MAX_LENGTH)
    sequence = []
    for i in range(length):
        sequence.append(start + step * i)
    max_of_sequence = len(sequence) - 1
    random_number = randint(0, max_of_sequence)
    question = get_hidden_sequence(sequence, random_number)
    correct_value = sequence[random_number]
    return question, correct_value


# getting the hidden sequence
def get_hidden_sequence(sequence, random_number):
    question = ''
    for i in sequence:
        if i == sequence[random_number]:
            i = '..'
        question += str(i) + ' '
    return question
