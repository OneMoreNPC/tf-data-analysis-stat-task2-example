import pandas as pd
import numpy as np
from scipy.stats import chi2 

chat_id = 49479018 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
    loc = x.mean()
    sqr_s = 0
    for i in range(n):
        sqr_s += x[i]**2
    left = sqr_s / chi2.ppf((1-alpha / 2), df = 2*n)
    right = sqr_s / chi2.ppf((alpha / 2), df = 2*n)
    return np.sqrt(left/2) , \
           np.sqrt(right/2)
