from random import randint
from math import sqrt


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    answer = 'yes'
    divider = 2

    while divider <= sqrt(number):
        if number % divider == 0:
            answer = 'no'
            return answer
        divider += 1
    return answer


def get_game():
    example = randint(2, 100)
    right_answer = is_prime(example)

    return example, right_answer
