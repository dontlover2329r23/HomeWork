import pandas as pd
import numpy as np

with open('parameters.txt', 'r') as f:
    gamma_line = f.readline().strip()
    gamma = float(gamma_line.split('=')[-1].strip())
data = pd.read_csv('links.csv')
dict = data.groupby('from')['to'].apply(list).to_dict()
print(dict)
site_list = list(dict.keys())
size = len(dict)
print(f'{size} - количество сайтов')
matrix = np.zeros((size,size))
for i in range(size):
    for j in range(size):
        if site_list[j] in dict[site_list[i]]:
            matrix[i, j] = (1-size*gamma)/len(dict[site_list[i]])
        matrix[i, j] += gamma
Q = np.copy(matrix)
for i in range(2000):
    Q = np.dot(Q,matrix)
l = Q[0]
print(l)
sort_ind = np.argsort(l)[::-1]
sort_l = l[sort_ind]
for i, value in enumerate(sort_l):
    index = sort_ind[i]
    print(f"Значение {value}, сайт {site_list[index]}")
