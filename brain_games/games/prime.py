from random import randint
UNIQ_GAME_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(random_number):
    '''check if number is prime or not'''
    if random_number == 1:
        return True
    else:
        for i in range(2, int(random_number ** 0.5) + 1):
            if random_number % i == 0:
                return False
        return True


def generate_question_and_true_answer():
    question = randint(1, 100)
    if prime_check(question):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return question, true_answer
