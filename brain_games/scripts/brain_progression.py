#!/usr/bin/env python


from brain_games.engine import main_engine
from brain_games.games.progression import get_question, RULES


def main():

    # calling the question and the answer func from the progression algorithm
    main_engine(get_question, RULES)


if __name__ == '__main__':
    main()
