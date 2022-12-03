from random import randint, choice


question = 'What number is missing in the progression?'


def get_game():
    start = randint(0, 100)
    step = randint(1, 20)
    progression = [i for i in range(start, step * 10 + start, step)]
    right_answer = choice(progression)
    progression[progression.index(right_answer)] = '..'
    example = ' '.join(map(str, progression))

    return example, str(right_answer)
