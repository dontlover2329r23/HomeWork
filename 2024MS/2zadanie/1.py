import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Заданная выборка данных
data = [122,116.8,118.5,118.5,121,121.5,126,121.8,121.5,122.9,119,121,121,125.9,122,119.2,126,125,116.7,121,120,124.5,
121,127,118.3,117,120,117.8,120.8,119,125,120.6,120.2,122,118.7,120,121.4,119.5,125,123,118,122,122.5,119,123,117.2,
119.5,125.1,124.3,122.8,124,121.5,126.5,122.5,123,115,126.2,120.5,123,122.5,123,121.5,116.9,123.8,121.5,118,121.7,
120,122.5,123,121,122.5,119.5,122.5,120.5,121,121.2,118.9,124,123,119.2,119.5
]

def empirical_cdf(data):
    sorted_data = np.sort(data)
    n = len(sorted_data)
    y = np.arange(1, n + 1) / n
    return sorted_data, y

def theoretical_cdf(data):
    mu = np.mean(data)
    std = np.std(data,ddof=1)
    x = np.sort(data)
    y = norm.cdf(x, mu, std)
    return x, y

sorted_data_empirical, y_empirical = empirical_cdf(data)
x_theoretical, y_theoretical = theoretical_cdf(data)

plt.step(sorted_data_empirical, y_empirical, label='Empirical CDF')
plt.plot(x_theoretical, y_theoretical, label='Theoretical CDF', linestyle='--')
plt.xlabel('Data')
plt.ylabel('CDF')
plt.title('Empirical vs Theoretical Cumulative Distribution Function')
plt.legend()
plt.grid(True)
plt.show()

# Нахождение абсолютного расхождения между эмпирической и теоретической ФР
absolute_difference = np.abs(y_empirical - y_theoretical).max()
print("Absolute Difference between Empirical and Theoretical CDF:", absolute_difference)
