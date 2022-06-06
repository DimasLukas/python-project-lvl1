import prompt
import random
Uniq_game_message = 'What is the result of the expression?'


def question_for_user():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    symbol = random.choice(['+', '-', '*'])
    if symbol == '+':
        result = first_number + second_number
    if symbol == '-':
        result = first_number - second_number
    if symbol == '*':
        result = first_number * second_number
    print("Question: ", first_number, symbol, second_number)
    user_answer = prompt.integer('Your answer: ')
    return(result, user_answer)
