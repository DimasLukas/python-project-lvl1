from random import randint
import prompt
Uniq_game_message = 'What number is missing in the progression?'


def question_for_user():
    progression = []
    number = randint(0, 10)
    number_add = randint(1, 10)
    progression_length = 5 + randint(0, 5)
    for i in range(progression_length):
        progression.append(number)
        number = number + number_add
    hidden_number = randint(0, progression_length - 1)
    number_to_calculate = progression[hidden_number]
    progression[hidden_number] = '..'
    print(*progression)
    user_answer = prompt.integer('Your answer: ')
    return (number_to_calculate, user_answer)
