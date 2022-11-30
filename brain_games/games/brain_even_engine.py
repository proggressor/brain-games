from random import randint


question = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game():
    example = randint(0, 100)

    if example % 2 == 0:
        rigth_answer = 'yes'
    else:
        rigth_answer = 'no'

    return example, rigth_answer
