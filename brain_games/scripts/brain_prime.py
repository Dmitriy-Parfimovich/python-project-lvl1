#!/usr/bin/env python


from brain_games.engine import main_engine
from brain_games.prime import get_question


def main():

    # calling the question and answer function from the algorithm the prime
    main_engine(get_question)


if __name__ == '__main__':
    main()
