#!/usr/bin/env python
import prompt
# import random
from brain_games.games import prime


def intro():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def main():
    name = intro()
    iterator = 0
    prime.main(name, iterator)
    return


if __name__ == '__main__':
    main()
