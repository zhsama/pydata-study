# @Version : Python3.6
# @Time    : 2018/6/3 16:56
# @Author  : zhcf1ess
# @Site    : 
# @File    : 数据库风格的 DataFrame 合并.py
# @Software: PyCharm
import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'key': ['b', 'b', 'a', 'c', 'a', ' a', 'b'],
    'data1': range(7)
})
df2 = pd.DataFrame({
    'key': ['a', 'b', 'd'],
    'data2': range(3)
})
# print(df1)
# print(df2)
# print(pd.merge(df1, df2))
# print(pd.merge(df1, df2, on='key'))

# 键名不同 分别制定键名
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
print(df3)
print(df4)
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

# 外连接
# print(pd.merge(df1, df2, how='outer'))
# print(pd.merge(df3, df4, left_on='lkey', right_on='rkey', how='outer'))

# 多对多连接
df5 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', ' b'], 'data1': range(6)})
df6 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'], 'data2': range(5)})
# pd.merge(df5, df6, how='inner')

# 多个键合并 传入键名列表
left = pd.DataFrame({
    'key1': ['foo', 'foo', 'bar'],
    'key2': ['one', 'two', 'one'],
    'lval': [1, 2, 3]
})
right = pd.DataFrame({
    'key1': ['foo', 'foo', 'bar', 'bar'],
    'key2': ['one', 'one', 'one', 'two'],
    'rval': [4, 5, 6, 7]
})
# print(pd.merge(left, right, on=['key1', 'key2'], how='inner'))

# print(pd.merge(left, right, on='key1'))
# print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))
