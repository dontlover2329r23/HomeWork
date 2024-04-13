import numpy as np # Импорт библиотеки numpy для работы с массивами
import matplotlib.pyplot as plt # Импорт библиотеки matplotlib для построения графиков
N = 1000 # Количество экспериментов
alpha = 0.01 # Уровень значимости
lambda_rate = 12.6 # Интенсивность потока запросов
theta = 1 / 6.0 # Параметр экспоненциального распределения
Qs = [] # Список для хранения максимального количества активных запросов
time_limit = 8 # Предел времен
#Генерация экспоненциальных точек и определение максимального количества активных запросов
for i in range(N):
    tau = 0
    taus = []
    while tau <= time_limit:
        tau += np.random.exponential(1 / lambda_rate)
        if tau <= time_limit:
            taus.append(tau)
    gammas = np.random.exponential(theta, size=len(taus))
    T = np.linspace(0, max(taus), num=100)
    max_active = 0
    for t in T:
        active_requests = sum((t >= taus[j]) and (t <= taus[j] + gammas[j]) for j in range(len(taus)))
        if active_requests > max_active:
            max_active = active_requests
    Qs.append(max_active)
#Сортировка максимального количества активных запросов
Qs.sort(reverse=True)
s_values = []
probabilities = []
s_min = 0
#Определение минимального количества единиц обслуживания, удовлетворяющего уровню значимости
for s in range(max(Qs) + 1):
    probability = sum(q > s for q in Qs) / N
    probabilities.append(probability)
    s_values.append(s)
    if probability <= alpha:
        s_min = s
        break

#Построение графика
plt.figure(figsize=(10, 6))
plt.plot(s_values, probabilities, marker='o', linestyle='-', color='black')
plt.axhline(y=alpha, color='red', linestyle='--')
plt.axvline(x=s_min, color='blue', linestyle='--')
plt.title('Вероятность превышения количества активных запросов')
plt.xlabel('Количество единиц обслуживания ')
plt.ylabel('Вероятность превышения s')
plt.grid(True)
plt.show()

print(f"Минимальное количество обслуживающих элементов s: {s_min}")#Вывод минимального количества единиц обслуживания
