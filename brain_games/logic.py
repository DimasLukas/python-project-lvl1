import prompt


def welcome_user():
    '''function makes greeting and asks for username'''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(user_answer, result):
    ''' Check for correct answer'''
    if user_answer == result:
        print('Correct!')
        return (True)
    else:
        print(f"{user_answer} is wrong answer; (. Correct answer was {result}.")
        return (False)


def play_game(Uniq_game_message, question_for_user):
    ''' 3 rounds of game and last messages for user'''
    name = welcome_user()
    print(Uniq_game_message)
    number_of_games = 1
    while number_of_games <= 3:
        result, user_answer = question_for_user()
        checked_answer = check_answer(user_answer, result)
        if checked_answer:
            if number_of_games == 3:  # check if it is last game
                print(f'Congratulations, {name}!')
                break
            number_of_games += 1
        else:
            print(f"Let's try again, {name}!")
            break
