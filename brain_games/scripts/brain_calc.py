#!/usr/bin/env python


from brain_games.games.engine import main_engine
from brain_games.games.calc import get_question


def main():

    # calling the question and answer function from the algorithm the calc
    main_engine(get_question)


if __name__ == '__main__':
    main()
