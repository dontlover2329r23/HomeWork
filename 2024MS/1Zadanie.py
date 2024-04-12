import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Data = pd.read_csv('r1z1.csv')
n=len(Data)
mean=sum(Data['X']) / n
min_elem= Data['X'].min()
Min_elem_floor=math.floor(min_elem)
max_elem= Data['X'].max()
Max_elem_ceil=math.ceil(max_elem)
srednee=  sum(Data['X']) / n
plt.hist(Data['X'], bins=[_ + 0.05 for _ in range(Min_elem_floor, Max_elem_ceil + 1, 1)], color='blue', edgecolor='red')
plt.title('Гистограмма прочности')
plt.show()
Data_sort= np.sort(Data['X'])
Value = np.arange(1, n+ 1) / n
mean_x = np.mean(Data_sort)
plt.figure(figsize=(10, 6))
plt.step(Data_sort, Value , where='post')
plt.axhline(y=0, color='gray', linewidth=0.5)
plt.axvline(x=mean_x, color='gray', linestyle='--', linewidth=0.5)
plt.show()
if n % 2 == 1:
    median  = Data_sort[n // 2]
else:
     median  = (Data_sort[n // 2 - 1] + Data_sort[n // 2]) / 2
dispersion = sum(math.pow((xi - mean), 2) for xi in Data['X']) / n
std_dev = dispersion ** 0.5
range_ = max_elem - min_elem
quart1 = Data['X'].quantile(0.25)
quart3 = Data['X'].quantile(0.75)
iqr = quart3 - quart1
mode = Data['X'].mode().values[0]
assim = (1 / n) * sum(math.pow((xi - srednee), 3) for xi in Data['X']) / (math.pow(std_dev, 3))
print("Объём выборки:", n)
print("Среднее:" ,srednee)
print("Медиана:" ,median)
print("Дисперсия:",dispersion)
print("Стандартное отклонение:",std_dev)
print("Минимум:", min_elem)
print("Максимум:", max_elem)
print("Размах:", range_)
print("Квартиль 1/4:", quart1)
print("Квартиль 3/4:",quart3)
print("Интерквартильная широта:", iqr)
print("Мода:",mode)
print("Асимметрия:", assim)
