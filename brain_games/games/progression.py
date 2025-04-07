"""
Этот модуль отвечает за логику игры "Геометрическая прогрессия"
"""

import random


DESCRIPTION = "What number is missing in the progression?"

def generate_question():
    """
    Функция генерирующая набор чисел для игры
    """
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = 10
    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, answer
