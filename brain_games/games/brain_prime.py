from random import randint
import prompt
Uniq_game_message = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(number_for_user):
    '''check if number is prime or not'''
    for i in range(2, int(number_for_user ** 0.5) + 1):
        if number_for_user % i == 0:
            return False
    return True


def question_for_user():
    number = randint(1, 100)
    print("Question: ", number)
    user_answer = prompt.string('Your answer: ')
    if prime(number):
        result = 'yes'
    else:
        result = 'no'
    return(result, user_answer)
