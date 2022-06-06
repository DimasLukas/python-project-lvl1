from random import randint
import prompt
Uniq_game_message = 'Find the greatest common divisor of given numbers.'


def question_for_user():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    print("Question: ", first_number, ' ', second_number)
    user_answer = prompt.integer('Your answer: ')
    while second_number > 0:
        first_number, second_number = second_number, first_number % second_number
    result = first_number
    return(result, user_answer)
