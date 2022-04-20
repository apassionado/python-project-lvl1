from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    random_number = randint(1, 100)
    truth = 'yes' if random_number % 2 == 0 else 'no'
    c = f'Question: {random_number}'
    return truth, c
