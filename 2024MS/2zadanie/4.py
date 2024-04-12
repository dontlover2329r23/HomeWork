import math

import numpy as np
from scipy import stats


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
    for i in range(1,len_ + 1):
        res += pow(data[i-1], 2)
    res *= 1/len_
    res -= np.mean(data)**2

    return (len_/(len_ - 1)) * res

def std_dev_(dispersion_):
    return dispersion_**0.5

# Преобразование данных из строк с запятыми в числа с точками
data = np.array(data)

# Определение размера выборки
n = len(data)

def Xmean_and_v(data, left_bound, right_bound):
    data_1 = []

    for i in range(0, len(data)):
        if ((data[i] <= right_bound + 0.05) and (data[i] > left_bound + 0.05)):
            data_1.append(data[i])

    data_1 = sorted(data_1)

    v = len(data_1)

    return [(left_bound + right_bound) / 2, v]

def mean_group(data, group_boudns):
    r = len(group_boudns)
    res = 0

    for j in range(0, r - 1):
        multipliers = Xmean_and_v(data, group_boudns[j], group_boudns[j + 1])

        res += multipliers[0] * multipliers[1]

    return (1 / len(data)) * res
disp = dispersion(data)
std_dev = std_dev_(disp)

print(f"Дисперсия {disp}")
print(f"Стандартное отклонение {std_dev}\n")

def dispersion_group(data, group_bounds):

    r = len(group_bounds)
    res = 0

    for j in range(0, r - 1):
        multipliers = Xmean_and_v(data, group_bounds[j], group_bounds[j + 1])

        res += multipliers[1] * (multipliers[0])**2

    res *= (1/len(data))
    res -= (mean_group(data, group_bounds))**2

    return res

set_ = set()
for i in range(0,len(data)):
    set_.add(math.floor(data[i]))
r = len(set_)
set_ = sorted(set_)
disp_gr = dispersion_group(data, set_)
std_dev_gr = std_dev_(disp_gr)
print(f"Дисперсия по группированным данным {disp_gr}")
print(f"Ст.отклонение по группированным данным {std_dev_gr}\n")
confidence_level = 0.9
alpha = 1 - confidence_level
df=n-1
lower_quantile = stats.chi2.ppf(alpha, df)
confidence_bounds= ((n-1)*disp)/(lower_quantile)
print(f"Доверительные границы для дисперсии {confidence_bounds}")
print(f"Доверительные границы для станд отклонения {confidence_bounds**0.5}")