from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return answer


def get_game():
    example = randint(0, 100)
    right_answer = is_even(example)

    return example, right_answer
