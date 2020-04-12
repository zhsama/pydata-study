# @Version : Python3.6
# @Time    : 2018/6/9 16:47
# @Author  : zhcf1ess
# @Site    : 
# @File    : 示例：用特定于分组的值填充缺失值.py
# @Software: PyCharm
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(6))
# print(s)
s[::2] = np.nan
# print(s)
# print(s.fillna(s.mean()))

states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
# print(data)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
# print(data.groupby(group_key).mean())

# fill_mean = lambda g: g.fillna(g.mean())
# print(data.groupby(group_key).apply(fill_mean))

fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
# print(data.groupby(group_key).apply(fill_func))
