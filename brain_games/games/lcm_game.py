"""
Этот модуль отвечает за логику игры "Наименьший общий квадрат"
"""

import random
import math


DESCRIPTION = "Find the smallest common multiple of given numbers."

def generate_question():
    """
    Эта функция отвечает за генерацию чисел для игры в НОК
    """
    nums = [random.randint(1, 20) for _ in range(3)]
    question = " ".join(map(str, nums))
    lcm_result = math.lcm(*nums)
    return question, str(lcm_result)
