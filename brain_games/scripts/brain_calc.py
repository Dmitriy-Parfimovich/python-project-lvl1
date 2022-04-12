#!/usr/bin/env python


from brain_games.games.engine import main_engine
from brain_games.games.calc import get_question, rules


def main():

    # calling the question and the answer function from the calc algorithm
    main_engine(get_question, rules)


if __name__ == '__main__':
    main()
