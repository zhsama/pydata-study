# @Version : Python3.6
# @Time    : 2018/6/8 20:04
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import random

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# print(np.random.randn(16))
# df = pd.DataFrame(np.random.randn(16).reshape(4, 4), index=list('abcd'), columns=list('1234'))
# print(df)
# random.seed('1234')
# data = pd.Series(list('asdfghjlkqwertyu'), index=np.arange(16))
# print(data)

df = pd.DataFrame(
    {
        'key1': ['a', 'a', 'b', 'b', 'a'],
        'key2': ['one', 'two', 'one', 'two ', 'one'],
        'data1': np.random.randn(5),
        'data2': np.random.randn(5)
    }
)
# print(df)
print(df.stack())
# print(df.index)
# print(df.index.name)

# 按 key1 进行分组，并计算 data1 列的平均值
grouped = df['data1'].groupby(df['key1'])  # SeriesGroupBy对象
# 数据（Series）根据分组键进行了聚合，产生了一个新的 Series，其索引为 key1 列中的唯一值
# 未进行计算 只是含有一些有关分组键 df['key1']的中间数据

# 求平均值
# print(grouped.mean())

# 传入多个列表
# means = df['data1'].groupby([df['key1'], df['key2']]).mean()
# print(means)
# print(means.unstack())

# 分组键可以是任何长度适当的数组
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
means = df['data1'].groupby([states, years]).mean()
# print(means)
# print(means.unstack())
# print(type(means))

# 还可以将列名（可以是字符串、数字或其他 Python 对象）用作分组键
# print(df.groupby('key1').mean())
# print(df.groupby(['key1', 'key2']).mean())
print(df.groupby(['key1', 'key2']).size())  # 返回一个含有分组大小的series

