import pandas as pd
import numpy as np

from scipy.stats import chi2 


chat_id = 49479018 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x) 
    alpha = 1 - p 
    sqr_sum = 0 
    for i in range(n): 
        sqr_sum = sqr_sum + x[i]**2 
    left_i = sqr_sum / chi2.ppf((1-alpha / 2), df = 2*n) 
    right_i = sqr_sum / chi2.ppf((alpha / 2), df = 2*n) 
    return np.sqrt(left_i/2) , \ 
           np.sqrt(right_i/2)