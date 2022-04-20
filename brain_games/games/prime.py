from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    last = randint(2, 100)
    truth = 'yes'
    for i in range(2, last):
        if last % i == 0:
            truth = 'no'
    c = f'Question: {last}'
    return truth, c
