import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    rounds_count = 3
    for i in range(rounds_count):
        truth = game.get_question_and_answer()
        print(truth[1])
        bet = prompt.string('Your answer: ')
        if bet == truth[0]:
            print('Correct!')
        else:
            print(f"'{bet}' is wrong answer ;(. Correct answer was '{truth}'.")
            print(f"Let's try again, {name}!")
            return
    return print(f'Congratulations, {name}!')
