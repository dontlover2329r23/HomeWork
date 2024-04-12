import math
import numpy as np
from scipy.stats import binom


# Данные
# Заданная выборка данных
data = [122,116.8,118.5,118.5,121,121.5,126,121.8,121.5,122.9,119,121,121,125.9,122,119.2,126,125,116.7,121,120,124.5,
121,127,118.3,117,120,117.8,120.8,119,125,120.6,120.2,122,118.7,120,121.4,119.5,125,123,118,122,122.5,119,123,117.2,
119.5,125.1,124.3,122.8,124,121.5,126.5,122.5,123,115,126.2,120.5,123,122.5,123,121.5,116.9,123.8,121.5,118,121.7,
120,122.5,123,121,122.5,119.5,122.5,120.5,121,121.2,118.9,124,123,119.2,119.5
]



n = len(data)

Q = 0.975
alpha = 1 - Q
j_values = []
for s in range(n+1):
    prob_diff = binom.cdf(n - s, n, 0.5) - binom.cdf(s - 1, n, 0.5)
    if prob_diff >= 1 - (alpha/2):
        j_values.append(s)
max_j = max(j_values)
data = np.array(data)
data = np.sort(data)
lower_bound = data[max_j]
upper_bound = data[n - max_j-1]
if n % 2 == 0:
    median = (data[n//2 - 1] + data[n//2]) / 2
    print(f"Точечная оценка медианы:: {median}")
else:
    median = data[n//2]
    print(f"Точечная оценка медианы:: {median}")
print("Двусторонний доверительный интервал для медианы:", (max_j,n-max_j-1),(lower_bound, upper_bound))

