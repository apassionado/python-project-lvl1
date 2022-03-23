from random import randint
import prompt
import math


def test():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    result = math.gcd(rand_num1, rand_num2)
    print(f'Question: {rand_num1} {rand_num2}')
    bet = prompt.string('Your answer: ')
    truth = str(result)
    return bet, truth


def main(name, iterator):
    if iterator > 2:
        return print(f'Congratulations, {name}!')
    else:
        outcome = test()
        bet = outcome[0]
        truth = outcome[1]
        if bet == truth:
            print('Correct!')
            iterator += 1
            main(name, iterator)
        else:
            print(f"'{bet}' is wrong answer ;(. Correct answer was '{truth}'.")
            print(f"Let's try again, {name}!")
            return  # перевод каретки внутри print? \n
    return
