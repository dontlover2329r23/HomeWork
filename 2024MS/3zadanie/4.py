import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
# Данные
group1 = [47.7, 48.4, 37.3, 61.7, 49.6, 50.3, 44.3, 58.8, 24.2, 37.3, 44, 57, 64.1, 31.1, 51.5, 48.7, 33.8, 53.3, 55.4, 45, 41.3, 22.2, 25.3, 67.6, 63.6, 43.8, 58]
group2 = [-4.1, 4, 33.5, 3.6, 7.1, -0.1, 16.2, 29.6, 20.1, 5.7, 5.1, -1.9, -8.6, -8.1, 21.8, 12.7, 16.4, 20.6, 19.6, 7.3, 18.8, 27, -4.2, 19.3, 12.9, 12.9, 2.3, 5.7, -4.2, 3.1, 26.1, 16]

# Критерий Вилкоксона
n1 = len(group1)
n2 = len(group2)
print(n1,n2)
ranks = np.concatenate([group1, group2])
ranks = np.argsort(np.argsort(ranks)) + 1
W = np.sum(ranks[:n1])
print("Сумма рангов 1-й выборки W:", W)
# Параметры нормального распределения
mu_W = n1 * (n1 + n2 + 1) / 2
sigma_W = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
print(mu_W ,sigma_W )
# Вычисление p-value
p_value = norm.cdf(W, loc=mu_W, scale=sigma_W)

# Уровень значимости
alpha = 0.1
print(f"p-value={p_value}")
# Находим квантиль порядка alpha
quantile = norm.ppf(alpha)

# Находим критическую константу C_alpha
C_alpha = sigma_W  * quantile + mu_W

print("Критическая константа C_alpha:", C_alpha)
# Кривая ЭЦФ для новых ламп (синяя линия)
plt.figure()
plt.step(np.sort(group1), np.linspace(0, 1, len(group1)), color='orange', label='Старые лампы')
plt.step(np.sort(group2), np.linspace(0, 1, len(group2)), color='blue', label='Новые лампы')
plt.xlabel('Переменная')
plt.ylabel('ЭЦФ')
plt.legend()
plt.show()
