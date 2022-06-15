import prompt

def play_game(game):
    """ 3 rounds of game and last messages for user"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.UNIQ_GAME_MESSAGE)
    NUMBER_OF_GAMES = 3
    rounds = 1
    for rounds in range(NUMBER_OF_GAMES):
        question, true_answer = game.generate_question_and_true_answer()
        print(f"Question:  {question}")
        user_answer = prompt.string('Your answer: ')

        if user_answer == true_answer:
            print('Correct!')
            rounds += 1
        else:
            print(f"{user_answer} is wrong answer; (. Correct answer was {true_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')