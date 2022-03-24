#!/usr/bin/env python
import prompt
# import random
from brain_games.games import progression


def intro():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    return name


def main():
    name = intro()
    iterator = 0
    progression.main(name, iterator)
    return


if __name__ == '__main__':
    main()
