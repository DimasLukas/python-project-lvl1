from random import randint
GAME_RULES = 'Answer "yes" if given number is prime. ' \
             'Otherwise answer "no".'


def is_prime(number):
    '''check if number is prime or not'''
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_right_answer():
    question = randint(0, 100)
    if is_prime(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
