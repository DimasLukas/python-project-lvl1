from random import randint
import prompt


def welcome_user():
    '''function makes greeting and asks for username'''
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def correct_answer(number_for_user):
    '''function checks if generated int number is even or
       not and makes return yes or no'''
    return 'no' if number_for_user % 2 else 'yes'


def make_question():
    '''function creates random int number from 0 to 100
       and ask user to give answer '''
    number_for_user = randint(1, 100)
    question = print(f'Question: {number_for_user}')
    answer = correct_answer(number_for_user)
    return (question, answer)


def check_answer(user_answer, correct_answer):
    '''function checks user answer vs correct answer'''
    if user_answer == correct_answer:
        message = 'Correct!'
        return (True, message)
    message = f'{user_answer} is wrong answer; (. Correct answer was {correct_answer}.'
    return (False, message)


def play_brain_even():
    '''function for starting game process'''
    name = welcome_user()
    print('')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_games = 1
    while number_of_games <= 3:
        question, answer = make_question()
        user_answer = input('Your answer: ')
        correct, message = check_answer(user_answer, answer)
        if correct:
            print(message)
            if number_of_games == 3:  # check if it is last game
                print(f'Congratulations! {name}')
            number_of_games += 1
        else:
            print(message)
            print('')
            print(f"Let's try again, {name}!")
            break
