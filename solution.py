import pandas as pd
import numpy as np
from hyppo.ksample import MMD


chat_id = 392609262 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    return MMD(compute_kernel="rbf", gamma=1).test(x, y)[1] < 0.06
