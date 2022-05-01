from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = randint(2, 100)
    answer = 'yes'
    for i in range(2, question):
        if question % i == 0:
            answer = 'no'
    return answer, question
