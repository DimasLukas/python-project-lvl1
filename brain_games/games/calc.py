import random
from operator import add, sub, mul
GAME_RULES = 'What is the result of the expression?'


def generate_question_and_right_answer():
    operators = {
        '+': add,
        '-': sub,
        '*': mul
    }
    keys = list(operators)
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    picked_operator = random.choice(keys)
    right_answer = str(operators[picked_operator](first_number, second_number))
    question = f"{first_number} {picked_operator} {second_number}"
    return question, right_answer
