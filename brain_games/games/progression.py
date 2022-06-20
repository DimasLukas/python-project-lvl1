from random import randint
GAME_RULES = 'What number is missing ' \
             'in the progression?'


def generate_question_and_right_answer():
    progression = []
    current_element = randint(0, 10)
    number_increment = randint(1, 10)
    progression_length = 10
    for _ in range(progression_length):
        progression.append(current_element)
        current_element = current_element + number_increment
    random_index = randint(0, progression_length - 1)
    right_answer = str(progression[random_index])
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return question, right_answer
