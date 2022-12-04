from random import randint
from math import sqrt


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game():
    example = randint(0, 100)
    right_answer = 'yes'
    divider = 2

    while divider <= sqrt(example):
        if example % divider == 0 or example in [0, 1]:
            right_answer = 'no'
            return example, right_answer
        divider += 1

    return example, right_answer
