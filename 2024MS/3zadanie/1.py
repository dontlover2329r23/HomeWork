import numpy as np
import scipy.stats as stats
import scipy.optimize as optimize
from scipy.stats import t
# данные
before = [152.5, 152.4, 171.4, 169.9, 157.4, 160.3, 144.7, 170.1, 136.7, 145.3, 158.4, 185.6, 156.4, 159.1, 164.1, 166.1, 150.9, 146.2, 158.5, 155, 160.6, 170, 160, 168.2, 171.4, 161.3, 154.7, 155, 163, 158.6, 159.4, 158.8, 185.4, 156.9, 159.8, 151.5, 162.7, 161.7, 165.6, 163.1, 165.8, 170.3, 156.6, 163.5, 154.9, 152.7, 150.7, 158.8, 158.5, 167.4, 146.7, 160.8, 147.9, 168.5, 159.3, 160.5, 160.7, 138.1, 152.4, 154.4, 147.1]
after = [161.5, 161.9, 170.1, 163, 157.8, 163.3, 155.7, 169.7, 150.5, 150.6, 158.4, 182.8, 163.3, 153.4, 171.1, 152, 145.7, 146.8, 159.9, 156.6,
         157.5, 164.7, 161.8, 160.6, 162, 162.2, 145.4, 159.8, 161.9, 151.8, 157.1,164.9 ,170.2 ,173.6 ,147.7 ,159.9 ,157.5 ,165.9 ,166.4 ,158.3 ,164.9 ,170.9 ,161.2 ,158.4 ,160 ,152.8 ,151.7 ,168.1 ,155.9 ,165.1 ,145.7 ,162.6 ,151 ,167 ,163.4 ,163.5 ,159.1 ,138 ,162.9 ,159.4 ,148.6]

# уровень значимости
alpha = 0.1
print(f"OбЪём выборки  изначально={len(before)}, после= {len(after)}")
# вычисление среднего и дисперсии разностей
diff = np.array(before) - np.array(after)
mean_diff = np.mean(diff)
var_diff = np.var(diff)
print(f"Среднее изначально={np.mean(before)}, после= {np.mean(after)}, И разность={mean_diff}")
print(f"Станд.отклонение изначально={np.std(before,ddof=1)}, после= {np.std(after,ddof=1)}И разность={np.std(diff,ddof=1)}")

print(f"Стандартная ошибка среднего до : {np.std(before)/np.sqrt(len(before))}, после= {np.std(after)/np.sqrt(len(after))}И разность={np.std(diff)/np.sqrt(len(diff))}")
# статистика Стьюдента
T = mean_diff * np.sqrt(len(diff) -1) / np.sqrt(var_diff)
print(f"Статистика Стьюдента={T}")
def find_critical_constant(alpha):
    def equation(c):
        return 2 * (1 - stats.t.cdf(c, df=len(diff)-1)) - alpha

    t_critical = 0
    try:
        t_critical = optimize.brentq(equation, -10, 10)
    except ValueError:
        print("Критическая константа не найдена")

    return t_critical

t_critical = find_critical_constant(alpha)
print(f"Критическая константа  для alpha={alpha}: {t_critical}")
# Вычисление p-value
p_value = 2 * (1 - t.cdf(abs(T), df=60))

print(f"Критический уровень значимости p-value: {p_value}")
