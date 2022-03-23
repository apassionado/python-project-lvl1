#!/usr/bin/env python
import prompt
# import random
from ..games import gcd


def intro():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
#    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    return name


def main():
    name = intro()
    iterator = 0
    gcd.main(name, iterator)
    return


if __name__ == '__main__':
    main()
