#!/usr/bin/env python

import prompt


# just welcome function-------------------------------------------------
def welcome_user():

    name = prompt.string('May I have you name? ')
    print('Hello, {}!'.format(name))
    return name
