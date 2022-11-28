#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    test = 0
    while test < 3:
        question = randint(0, 1000)
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        right_answer = is_even(question)

        if right_answer == user_answer:
            print('Correct!')
            test += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            test = 0

    print(f'Congratulations, {name}!')


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    main()
