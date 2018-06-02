# @Version : Python3.6
# @Time    : 2018/6/1 16:30
# @Author  : zhcf1ess
# @Site    : 
# @File    : 填充缺失数据.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import nan as na

# series
data = pd.DataFrame([[1., 6.5, 3.], [1., na, na], [na, na, na], [na, 6.5, 3.]])
# print(data.fillna(0))

# dataframe
frame = pd.DataFrame(np.random.randn(7, 3))
frame.iloc[:4, 1] = na
frame.iloc[:2, 2] = na
# print(frame.fillna(0))
# print(frame.fillna({1: 0.5, 2: 0}))

# 在原对象上进行修改
# frame.fillna(0, inplace=True)
# print(frame)

# 对于重排索引reindexing有效的插值方法也适用于fillna
df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = na
df.iloc[4:, 2] = na

print(df.fillna(method='ffill'))

print(df.fillna(method='ffill', limit=2))