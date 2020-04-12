# @Version : Python3.6
# @Time    : 2018/9/10 17:34
# @Author  : zhcf1ess
# @Site    : 
# @File    : 估计线性模型.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf


def dnorm(mean, variance, size=1):
    if isinstance(size, int):
        size = size
    return mean + np.sqrt(variance) * np.random.randn(size)


np.random.seed(1234)

N = 100
X = np.c_[dnorm(0, 0.4, size=N), dnorm(0, 0.6, size=N), dnorm(0, 0.2, size=N)]

eps = dnorm(0, 0.1, size=N)

beta = [0.1, 0.3, 0.5]

y = np.dot(X, beta) + eps

# print(X[:5])
# print("============================================")
# print(y[:5])

# sm.add_constant(X)  添加一个截距到矩阵
# X_model = sm.add_constant(X)
# print(X_model)
model = sm.OLS(y, X)
result = model.fit()
# print(result.params)
# print(result.summary())
data = pd.DataFrame(X, columns=['col0', 'col1', 'col2'])
data['y'] = y
# print(data[:5])
results = smf.ols('y ~  col0  +  col1  +  col2', data=data).fit()
# print(results.params)
# print(results.tvalues)
print(result.predict(data[:5]))