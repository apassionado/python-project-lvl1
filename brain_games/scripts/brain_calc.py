#!/usr/bin/env python
import prompt
import random
from ..games import calc


def intro():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
#    print('Hello, {}!'.format(name))
    return name


def ops_order():
    return random.sample((0, 1, 2,), 3)


def main():
    name = intro()
    sequence = ops_order()
    iterator = 0
    calc.main(name, sequence, iterator)
    return


if __name__ == '__main__':
    main()
