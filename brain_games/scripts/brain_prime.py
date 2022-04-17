#!/usr/bin/env python


from brain_games.engine import main_engine
from brain_games.games.prime import get_question, rules


def main():

    # calling the question and the answer function from the prime algorithm
    main_engine(get_question, rules)


if __name__ == '__main__':
    main()
