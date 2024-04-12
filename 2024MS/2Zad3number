import math

import numpy as np
from scipy.stats import t

# Данные
# Заданная выборка данных
data = [122,116.8,118.5,118.5,121,121.5,126,121.8,121.5,122.9,119,121,121,125.9,122,119.2,126,125,116.7,121,120,124.5,
121,127,118.3,117,120,117.8,120.8,119,125,120.6,120.2,122,118.7,120,121.4,119.5,125,123,118,122,122.5,119,123,117.2,
119.5,125.1,124.3,122.8,124,121.5,126.5,122.5,123,115,126.2,120.5,123,122.5,123,121.5,116.9,123.8,121.5,118,121.7,
120,122.5,123,121,122.5,119.5,122.5,120.5,121,121.2,118.9,124,123,119.2,119.5
]



def dispersion(data):
    len_ = len(data)
    res = 0
    for i in range(1, len_ + 1):
        res += pow(data[i - 1], 2)
    res *= 1 / len_
    res -= np.mean(data) ** 2

    return (len_ / (len_ - 1)) * res
def std_dev_(dispersion_):
    return dispersion_ ** 0.5
data = np.array(data)
n = len(data)
set_ = set()
for i in range(0, len(data)):
    set_.add(math.floor(data[i]))
r = len(set_)
set_ = sorted(set_)
def Xmean_and_v(data, left_bound, right_bound):
    data_1 = []

    for i in range(0, len(data)):
        if ((data[i] <= right_bound + 0.05) and (data[i] > left_bound + 0.05)):
            data_1.append(data[i])

    data_1 = sorted(data_1)

    v = len(data_1)

    return [(left_bound + right_bound) / 2, v]
m = std_dev_(dispersion(data)) / (n ** 0.5)
Q = 0.99
alpha = 1 - Q
math_waiting = np.mean(data)
n1 = len(set_)
res = 0

for j in range(0, n1 - 1):
    multipliers = Xmean_and_v(data, set_[j], set_[j + 1])
    res += multipliers[0] * multipliers[1]
math_waiting_group = (1 / len(data)) * res

print(f"Объем {n}")
print(f"Матем.ожидание по полным данным {math_waiting}")
print(f"Матем.ожидание по группированным данным {math_waiting_group}")
beta = alpha / 2
t_quantile = t.ppf(1 - beta, n)
conf_b = [np.mean(data) - m * t_quantile,np.mean(data) + m * t_quantile]
print(f"{Q * 100}%-доверительный интервал для математического ожидания: m = {m}: {conf_b}")
