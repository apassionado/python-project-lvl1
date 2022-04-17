from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    diff = randint(1, 5)
    first = randint(1, 5)
    quise = first + (randint(0, 9) * diff)
    after_last = first + (10 * diff)
    test_string = ''
    a = ''
    for i in range(first, after_last, diff):
        a = '..' if i == quise else str(i)
        test_string = f'{test_string} {a}'
    print(f'Question:{test_string}')
    truth = str(quise)
    return truth
