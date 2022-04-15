import random
import prompt


DESCRIPTION = 'What is the result of the expression?'

ops_sequence = random.sample([0, 1, 2], 3)


def test():
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    m = ops_sequence.pop(0)
    if m == 1:
        result = rand_num1 + rand_num2
        print(f'Question: {rand_num1} + {rand_num2}')
    if m < 1:
        result = rand_num1 - rand_num2
        print(f'Question: {rand_num1} - {rand_num2}')
    if m > 1:
        result = rand_num1 * rand_num2
        print(f'Question: {rand_num1} * {rand_num2}')
    bet = prompt.string('Your answer: ')
    truth = str(result)
    return bet, truth
