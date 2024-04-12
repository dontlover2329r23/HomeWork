import math
import numpy as np
from scipy import stats
from scipy.stats import norm
import scipy.stats
import statsmodels.stats as st
import statsmodels.stats.proportion as st
data = [116.7, 117.7, 120.1, 119.5, 119.6, 121.9, 122.6, 117.8, 120.1, 121.1, 121.7, 120.7, 119.7, 117.9, 115.3, 122.2, 124.6, 120.8, 123.9, 119.9, 122.9, 126.8, 120.2, 125.6, 125.2, 117.9, 113.1, 119.5, 119.5, 116.4, 119.0, 118.3, 118.7, 119.5, 123.1, 120.2, 122.5, 120.5, 120.3, 120.1, 117.4, 119.5, 122.2, 120.1, 118.2, 126.8, 119.2, 119.8, 121.8, 121.8, 118.0, 119.5, 123.7, 121.1, 120.5, 120.7, 119.5, 121.2, 119.1, 121.2, 120.2, 122.7, 120.7, 116.9, 121.1, 117.4, 119.2, 119.8, 122.9, 121.8, 118.1, 120.4, 119.3, 118.3, 117.2, 122.9, 118.5, 119.6, 121.1, 121.3, 122.6, 122.1, 119.5, 119.1]
n=len(data)
count=0
x_norm = 117.5
for j in data:
    if(j>x_norm):
        count+=1
p=count/n
print(f"Частотная (непараметрическая) оценка { p ,n,count}")
X = np.mean(data)
S = np.std(data)



p_hat = 1 - norm.cdf((x_norm - X) / S)

print("в предположении, что выборка поступила из нормального закона:", p_hat,X,S)
Q=0.975
#нижняя
alpha=1-Q
lower_confidence_interval = st.proportion_confint(count=sum(np.array(data) > x_norm), nobs=len(data), alpha=1-Q, method='beta')
print("Точная 97.5%-нижняя граница для p:", lower_confidence_interval[0])

m = (norm.cdf((x_norm - X) / S)*(1-norm.cdf((x_norm - X) / S)) / n)**0.5

tb = stats.norm.ppf(1-alpha)

upper_bound_assimp = (1-norm.cdf((x_norm - X) / S)) -m * tb
print(f"Асимптотическая нижняя граница {upper_bound_assimp}")


