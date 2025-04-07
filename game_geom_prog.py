"""
Этот модуль содержит в себе логику для игры 'Геометрическая прогрессия'
"""

import random


def generate_geometric_progression(start, ratio, length):
    """Генерирует геометрическую прогрессию."""
    return [start * (ratio ** i) for i in range(length)]

def get_missing_term(progression):
    """
    Заменяет случайное число на '..' в прогрессии и возвращает 
    индекс пропущенного числа и саму прогрессию.
    """
    missing_index = random.randint(0, len(progression) - 1)
    missing_value = progression[missing_index]
    progression[missing_index] = '..'
    return progression, missing_value

def play_game():
    """Основная функция игры."""
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)

    progression = generate_geometric_progression(start, ratio, length)

    progression_with_missing, missing_value = get_missing_term(progression)

    print("What number is missing in the progression?")
    print("Question:", ' '.join(map(str, progression_with_missing)))

    answer = int(input("Your answer: "))

    if answer == missing_value:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{missing_value}'.")
        print(f"Let's try again, {name}!")

    print(f"Congratulations, {name}!")

def main():
    """main func"""
    play_game()

if __name__ == "__main__":
    main()
