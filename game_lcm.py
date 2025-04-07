"""
Этот модуль содержит в себе логику для игры 'Наименьшее общее кратное'
"""

import math
import random


def lcm(a, b):
    '''Вычисляет НОК'''
    return abs(a * b) // math.gcd(a, b) # |a * b| / НОД(a, b)

def main():
    '''main func'''
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    print("Find the smallest common multiple of given numbers.")

    score = 0
    for _ in range(3):
        nums = [random.randint(1, 20) for _ in range(3)]
        print(f"Question: {' '.join(map(str, nums))}")

        correct_answer = lcm(lcm(nums[0], nums[1]), nums[2])

        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
