# @Version : Python3.6
# @Time    : 2018/6/17 20:52
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import random

data = pd.DataFrame({
    'x0': [1, 2, 3, 4, 5],
    'x1': [0.01, -0.01, 0.25, -4.1, 0.],
    'y': [-1.5, 0., 3.6, 1.3, -2.]
})
# print(data)
# print(data.columns)
# print(data.values)
df2 = pd.DataFrame(data.values, columns=['one', 'two', 'three'])
# print(df2)

df3 = data.copy()
# print(df3)
df3['strings'] = ['a', 'b', 'c', 'd', 'e']
# print(df3)
# print(df3.values)

model_cols = ['x0', 'x1']
# print(data.loc[:, model_cols].values)

data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'], categories=['a', 'b'])
# print(data)
dummies = pd.get_dummies(data.category, prefix='category')
# print(dummies)
data_with_dummies = data.drop('category', axis=1).join(dummies)
# print(data_with_dummies)

# random.seed(6485268)
# print(random.randint(0, 51))
# print(random.randint(0, 51))
