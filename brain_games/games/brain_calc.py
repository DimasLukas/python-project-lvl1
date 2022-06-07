import prompt
import random
from operator import add, mul, sub
Uniq_game_message = 'What is the result of the expression?'

operators = {
    '+': add,
    '-': sub,
    '*': mul
}
keys = list(operators)


def question_for_user():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    picked_operator = random.choice(keys)
    print("Question: ", first_number, picked_operator, second_number)
    result = (operators[picked_operator](first_number, second_number))
    user_answer = prompt.integer('Your answer: ')
    return(result, user_answer)
