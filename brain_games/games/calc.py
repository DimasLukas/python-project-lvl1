import random
from operator import add, sub, mul
UNIQ_GAME_MESSAGE = 'What is the result of the expression?'


def generate_question_and_true_answer():
    operators = {
        '+': add,
        '-': sub,
        '*': mul
    }
    keys = list(operators)
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    picked_operator = random.choice(keys)
    true_answer = str(operators[picked_operator](first_number, second_number))
    question = '{0} {1} {2}'.format(first_number, picked_operator, second_number)
    return question, true_answer
