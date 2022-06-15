from random import randint
UNIQ_GAME_MESSAGE = 'What number is missing in the progression?'


def generate_question_and_true_answer():
    progression = []
    number = randint(0, 10)
    number_add = randint(1, 10)
    progression_length = 10
    for i in range(progression_length):
        progression.append(number)
        number = number + number_add
    hidden_number = randint(0, progression_length - 1)
    true_answer = str(progression[hidden_number])
    progression[hidden_number] = '..'
    question = ' '.join(map(str, progression))
    return question, true_answer
