from random import randint
GAME_RULES = 'Find the greatest common divisor ' \
             'of given numbers.'


def find_gcd(first_number, second_number):
    while second_number > 0:
        first_number, second_number = \
            second_number, first_number % second_number
    return first_number


def generate_question_and_right_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = f'{first_number} {second_number}'
    right_answer = str(find_gcd(first_number, second_number))
    return question, right_answer
