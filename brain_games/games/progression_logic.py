from random import randint, choice


QUESTION = 'What number is missing in the progression?'


def progression_generator(start, step):
    row = [i for i in range(start, step * 10 + start, step)]
    answer = choice(row)
    return answer, row


def get_game():
    start = randint(0, 100)
    step = randint(1, 20)
    right_answer, progression = progression_generator(start, step)
    progression[progression.index(right_answer)] = '..'
    example = ' '.join(map(str, progression))

    return example, str(right_answer)
