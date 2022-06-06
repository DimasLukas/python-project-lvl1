import prompt
from random import randint
Uniq_game_message = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_for_user():
    number_for_user = randint(0, 100)
    result = print(f'Question: {number_for_user}')
    user_answer = prompt.string('Your answer: ')
    result = 'yes' if number_for_user % 2 == 0 else 'no'
    return (result, user_answer)
