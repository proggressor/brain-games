import prompt


def get_template(engine):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(engine.question)
    counter = 0
    while counter < 3:
        example, right_answer = engine.get_game()
        print(f'Question: {example}')
        answer = prompt.string('Your answer: ')

        if right_answer == answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            counter = 4

    if counter == 3:
        print(f'Congratulations, {name}!')
