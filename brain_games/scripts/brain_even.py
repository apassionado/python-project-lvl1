#!/usr/bin/env python
import prompt
from brain_games.games import even


def intro():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def main():
    name = intro()
    iterator = 0
    even.main(name, iterator)
    return


if __name__ == '__main__':
    main()
