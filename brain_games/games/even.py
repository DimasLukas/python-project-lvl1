from random import randint
GAME_RULES = 'Answer "yes" if the number is even, ' \
             'otherwise answer "no".'


def generate_question_and_right_answer():
    question = randint(0, 100)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return question, right_answer
