#!/usr/bin/env python

import prompt


def welcome_user():

    name = prompt.string('May I have you name? ')
    print('Hello, {}!'.format(name))
    return name
