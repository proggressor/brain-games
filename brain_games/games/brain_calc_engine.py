from random import randint, choice


question = 'What is the result of the expression?'


def get_game():
    first_arg = randint(0, 25)
    second_arg = randint(0, 25)
    operator = choice(['+', '-', '*'])
    example = f'{first_arg} {operator} {second_arg}'
    rigth_answer = eval(example)

    return example, str(rigth_answer)
