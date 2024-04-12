import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde, norm


# Заданная выборка данных
data = [122,116.8,118.5,118.5,121,121.5,126,121.8,121.5,122.9,119,121,121,125.9,122,119.2,126,125,116.7,121,120,124.5,
121,127,118.3,117,120,117.8,120.8,119,125,120.6,120.2,122,118.7,120,121.4,119.5,125,123,118,122,122.5,119,123,117.2,
119.5,125.1,124.3,122.8,124,121.5,126.5,122.5,123,115,126.2,120.5,123,122.5,123,121.5,116.9,123.8,121.5,118,121.7,
120,122.5,123,121,122.5,119.5,122.5,120.5,121,121.2,118.9,124,123,119.2,119.5
]
# Параметры гистограммы
X0 = 111.55
delta = 1
r = 18
# Гистограмма
bin_edges = np.linspace(X0, X0 + delta * r, r + 1)
plt.hist(data, bins=bin_edges, alpha=0.5, label='Гистограмма', density=True)

# Ядерная оценка плотности с ядром Гаусса
kde = gaussian_kde(data, bw_method='silverman')
bandwidth_silverman = kde.factor # Значение окна ядерной оценки по методу Сильвермана
plt.text(0.05, 0.95, f'Окно (Сильверман): {bandwidth_silverman:.2f}', ha='left', va='top', transform=plt.gca().transAxes)
x_range = np.linspace(min(data), max(data), 1000)
plt.plot(x_range, kde(x_range), label='Ядерная оценка плотности', linewidth=2)

# График нормальной плотности
mean, std = np.mean(data), np.std(data, ddof=1)
plt.plot(x_range, norm.pdf(x_range, mean, std), label='Нормальная плотность', linestyle='--')

plt.xlabel('Значения')
plt.ylabel('Плотность')
plt.title('Гистограмма и оценки плотности')
plt.legend()
plt.grid(True)
plt.show()