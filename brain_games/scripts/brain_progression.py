#!/usr/bin/env python


from brain_games.games.engine import main_engine
from brain_games.games.progression import get_question


def main():

    # calling the question and answer func from the algorithm the progression
    main_engine(get_question)


if __name__ == '__main__':
    main()
