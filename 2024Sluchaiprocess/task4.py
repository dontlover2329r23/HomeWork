import numpy as np
import matplotlib.pyplot as plt

# Параметры задачи
alpha = 1.1
delta_t = 0.001
n_xi = 200
time_points = [0.1, 0.3, 0.5, 0.7, 0.9]

# Генерация траекторий методом Эйлера-Маруямы
def generate_trajectory(alpha, delta_t, t_end):
    n_steps = int(t_end / delta_t)
    t = np.linspace(0, t_end, n_steps + 1)
    x = np.zeros(n_steps + 1)
    for i in range(n_steps):
        dw = np.random.normal(0, np.sqrt(delta_t))
        x[i + 1] = x[i] - (alpha / (1 - t[i])) * x[i] * delta_t + dw
    return t, x

# Генерация нескольких траекторий
trajectories = [generate_trajectory(alpha, delta_t, time_points[-1]) for _ in range(4)]

# Визуализация траекторий
plt.figure(figsize=(10, 6))
for t, x in trajectories:
    plt.plot(t, x)
plt.title('Траектории процесса ξ(t)')
plt.xlabel('Время t')
plt.ylabel('ξ(t)')
plt.grid(True)
plt.show()

# Оценка квантилей методом Монте-Карло
def monte_carlo_quantiles(alpha, delta_t, time_points, n_xi):
    trajectories = [generate_trajectory(alpha, delta_t, time_points[-1])[1] for _ in range(n_xi)]
    quantiles = {t: [] for t in time_points}
    for t in time_points:
        idx = int(t / delta_t)
        values = [traj[idx] for traj in trajectories]
        quantiles[t] = {
            '0.05': np.quantile(values, 0.05),
            '0.50': np.quantile(values, 0.50),
            '0.95': np.quantile(values, 0.95)
        }
    return quantiles

quantiles = monte_carlo_quantiles(alpha, delta_t, time_points, n_xi)

# Вывод квантилей
for t in time_points:
    print(f"Время {t}: 0.05 квантиль = {quantiles[t]['0.05']}, 0.50 квантиль = {quantiles[t]['0.50']}, 0.95 квантиль = {quantiles[t]['0.95']}")
