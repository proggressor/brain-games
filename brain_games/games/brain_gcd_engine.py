from random import randint


QUESTION = 'Find the greatest common divisor of given numbers.'


def get_game():
    first_arg = randint(0, 100)
    second_arg = randint(0, 100)
    example = f'{first_arg} {second_arg}'

    while first_arg != second_arg:

        if first_arg > second_arg:
            first_arg = first_arg - second_arg
        else:
            second_arg = second_arg - first_arg

    right_answer = first_arg

    return example, str(right_answer)
