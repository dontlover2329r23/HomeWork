import numpy as np
import matplotlib.pyplot as plt

# Данные
data_group1 = np.array([20.4, 13.1, 14.7, 17.3, 15.8, 18.3, 16.8, 16.8, 19.9, 17.3, 14, 18.4, 12.9, 16.3, 15.6, 18.5,
                        18.6, 14.1, 15.2, 13.6, 19.3, 15.8, 14.3, 18.6, 19.6, 15.4, 20.3, 14, 16.5, 17.8, 16.2, 17.9,
                        17.3, 13.2, 14.8, 20.1, 17.1, 17.6, 20, 14.3, 19.2, 16.1, 17.5, 13.5, 20.6, 13, 15.9, 15.6, 13.7,
                        18.3, 16.3, 14.3, 17.8, 13.3, 12.8, 17.1, 13.2, 12.8, 18.7, 17.7, 16.8, 15.9, 19.4, 16, 18.3,
                        20.5, 14.6, 15.3, 18.4, 20.1, 19.4, 20.4, 17.5, 14.5, 15.8, 18.8, 20.3, 13.9, 15.7, 14.4, 19.8,
                        13.8, 17.7, 17.4, 15.7, 18.6, 19, 14.1, 18.1, 18.9, 17.1, 19.5, 20.4, 19.5, 18.4, 19.8, 15.6,
                        17.7, 15.3, 13.8, 16, 16.5, 20.3, 20.1])

data_group2 = np.array([16.9, 15.4, 15.2, 15.4, 13.9, 17.4, 16.9, 14.1, 16.5, 19.2, 20.5, 15.3, 16.8, 20.5, 14.8,
                        16.1, 13.9, 15.5, 20.2, 15.1, 18.6, 19.7, 20.7, 15.7, 14.4, 17.1, 18.1, 12.9, 13.3, 20.4, 13.9,
                        19.6, 17.5, 13.8, 14.1, 17, 13.4, 14, 20, 13.6, 20.2, 19.2, 20.5, 19.2, 14.4, 20.2, 20.5, 16.3,
                        20.7, 15.8, 15.1, 16, 20.1, 16.2, 13.9, 17.2, 15.3, 15, 20.4, 12.9, 14.6, 13.7, 13.1, 20, 15, 15.2,
                        13.3, 13.4, 13.4, 15.7, 13.4, 17.8, 13.4, 20.6, 19, 14.5, 14, 17.1, 17.9, 18, 19.4, 14.8, 18.1,
                        17.9, 17.5, 13.8, 17.7, 18.6, 15.2, 19.3])

# Условия
alpha = 0.025
X0 = 13.7
delta = 1
r = 8
interval_bounds = np.linspace(X0 - delta, X0 + delta, r+1)
# Построение графиков
plt.figure(figsize=(8, 10))

plt.subplot(2, 1, 1)
plt.hist(data_group1, bins=interval_bounds, color='b', alpha=0.7, label='Group 1', edgecolor='black')
plt.legend()
plt.title('Frequency Distribution of Group 1')
plt.xlabel('Intervals')
plt.ylabel('Frequency')

plt.subplot(2, 1, 2)
plt.hist(data_group2, bins=interval_bounds, color='r', alpha=0.7, label='Group 2', edgecolor='black')
plt.legend()
plt.title('Frequency Distribution of Group 2')
plt.xlabel('Intervals')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# Вычисление статистики Хи-квадрат
observed_group1, _ = np.histogram(data_group1, bins=r)
observed_group2, _ = np.histogram(data_group2, bins=r)
observed_total = observed_group1 + observed_group2
n1 = len(data_group1)
n2 = len(data_group2)

chi2_statistic = n1*n2*np.sum((observed_total - (observed_group1*n1/n1) - (observed_group2*n1/n2))**2 / (observed_total))
degree_of_freedom = r - 1

print(f"Хи-квадрат статистика: {chi2_statistic}")
print(f"Степени свободы: {degree_of_freedom}")

# Определение критического значения и p-value
from scipy.stats import chi2

critical_value = chi2.ppf(1 - alpha, degree_of_freedom)
p_value = 1 - chi2.cdf(chi2_statistic, degree_of_freedom)

print(f"Критическое значение: {critical_value}")
print(f"P-value: {p_value}")
