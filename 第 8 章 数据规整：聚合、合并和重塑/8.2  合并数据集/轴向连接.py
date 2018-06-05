# @Version : Python3.6
# @Time    : 2018/6/5 16:54
# @Author  : zhcf1ess
# @Site    : 
# @File    : 轴向连接.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# numpy.array
arr = np.arange(12).reshape(3, 4)
# print(arr)
# print(np.concatenate([arr, arr], axis=1))

# serires
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
# print(pd.concat([s1, s2, s3]))  # 合并索引和值
# print(pd.concat([s1, s2, s3], axis=1))
# join='inner'
s4 = pd.concat([s1, s3])
# print(pd.concat([s1, s4], axis=1))
# print(pd.concat([s1, s4], axis=1, join='inner'))
# print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]))
# keys
# result = pd.concat([s1, s2, s3], keys=list('123'))
# print(result)
# axis=1时 keys
# print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))

# dataframe
# df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
# df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'], columns=['three', 'four'])
# print(pd.concat([df1, df2], axis=1, keys=list('ab')))
# print(pd.concat({'a': df1, 'b': df2}))
# print(pd.concat({'a': df1, 'b': df2}, axis=1))

# DataFrame 的行索引不包含任何相关数据
df1 = pd.DataFrame(np.arange(16).reshape(4, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.arange(12).reshape(4, 3), columns=['b', 'd', 'a'])
# print(df1)
# print(df2)
# print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], ignore_index=True))
print(pd.merge(df1, df2, how='outer',))
