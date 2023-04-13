import pandas as pd
import numpy as np


chat_id = 392609262 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, cr_val, pval = anderson_ksamp([x, y])
    if stat > cr_val[2]:
        return True
    else:
        return False
