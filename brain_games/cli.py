#!/usr/bin/env python

import prompt


# just welcome function-------------------------------------------------
def welcome_user():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
