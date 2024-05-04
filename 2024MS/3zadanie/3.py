from scipy import stats
from scipy.optimize import minimize
from scipy import stats
# Данные
data = ['B'	,'B',	'A',	'B',	'B',	'B',	'B',	'B',	'B',	'A',	'B',	'A',	'A',	'A',	'B',	'A',	'B',	'B',	'A',	'B',	'A',	'B',	'B',	'A',	'B',	'B',	'B',	'A',	'B',	'B',	'B',	'B',	'B',	'B',	'A',	'B',	'B',	'B',	'B',	'B',	'B',	'B',	'B',	'B',	'B',	'A',	'B',	'B',	'A',	'A',	'A',	'B',	'B',	'B',	'A',	'B',	'B',	'A',	'A',	'B',	'B',	'B'        ]

# Подсчет количества успешных исходов
successes = data.count('A')
total_trials = len(data)
print("Количество пациентов="+str(total_trials))
# Уровень значимости
alpha = 0.05
print(f"Частота появления A={successes/total_trials} , или {successes} из {total_trials}")
theta_0 = 0.7  # Гипотеза о вероятности успеха
critical_value = None

step = 0.01  # Шаг перебора

for c in range(int(total_trials/step) + 1):
    c_real = c * step
    if 1 - stats.binom.cdf(c_real-1, total_trials, theta_0) <= alpha:
        critical_value = c_real
        break

print(f"Критическая константа C_alpha: {critical_value}")
p_value=1-stats.binom.cdf(successes-1, total_trials, theta_0)
print(f"p-value: {p_value}")
