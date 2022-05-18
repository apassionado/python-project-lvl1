from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(q):
    if q == 1:
        return False
    for i in range(2, q // 2 + 1):
        if q % i == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return correct_answer, question
