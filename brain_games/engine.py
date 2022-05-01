import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    rounds_count = 3
    for i in range(rounds_count):
        answer, question = game.get_question_and_answer()
        print(f'Question: {question}')
        your_answer = prompt.string('Your answer: ')
        if your_answer != answer:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{answer}'.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    return print(f'Congratulations, {name}!')
