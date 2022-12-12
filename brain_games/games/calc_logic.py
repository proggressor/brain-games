from random import randint, choice


QUESTION = 'What is the result of the expression?'


def calc(first_arg, second_arg, operator):
    match operator:
        case '+':
            answer = first_arg + second_arg
        case '-':
            answer = first_arg - second_arg
        case '*':
            answer = first_arg * second_arg
    return answer


def get_game():
    first_arg = randint(0, 25)
    second_arg = randint(0, 25)
    operator = choice(['+', '-', '*'])
    example = f'{first_arg} {operator} {second_arg}'
    right_answer = calc(first_arg, second_arg, operator)
    return example, str(right_answer)
