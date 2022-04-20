import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    rounds_count = 3
    for i in range(rounds_count):
        question_and_answer = game.get_question_and_answer()
        question = question_and_answer[1]
        answer = question_and_answer[0]
        print(question)
        bet = prompt.string('Your answer: ')
        if bet == answer:
            print('Correct!')
        else:
            print(f"'{bet}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
