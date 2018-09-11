# @Version : Python3.6
# @Time    : 2018/9/10 18:03
# @Author  : zhcf1ess
# @Site    : 
# @File    : 估计时间序列过程.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

N = 1000
b0 = 0.8
b1 = -0.4
init_x = 4


def dnorm(mean, variance, size=1):
    if isinstance(size, int):
        size = size
    return mean + np.sqrt(variance) * np.random.randn(size)


values = [init_x, init_x]
noise = dnorm(0, 0.1, N)
for i in range(N):
    new_x = values[-1] * b0 + values[-2] * b1 + noise[i]
    values.append(new_x)

MAXLAGS = 5
model = sm.tsa.AR(values)
results = model.fit(MAXLAGS)
print(results.params)
