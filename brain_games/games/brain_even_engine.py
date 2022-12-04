from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    example = randint(0, 100)

    if example % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return example, right_answer
