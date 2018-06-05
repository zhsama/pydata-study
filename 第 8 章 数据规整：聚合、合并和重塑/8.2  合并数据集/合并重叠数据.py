# @Version : Python3.6
# @Time    : 2018/6/5 18:05
# @Author  : zhcf1ess
# @Site    : 
# @File    : 合并重叠数据.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from numpy import nan as na

a = pd.Series([np.nan, 2.5, na, 3.5, 4.5, na], index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64), index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = na
# print(a)
# print(b)
# 三元运算符
# print(np.where(pd.isnull(a), b, a))
# print(b[:-2].combine_first(a[2:]))
# res = b.combine_first(a)
# print(type(res))
# print(b.combine_first(a))

# dataframe
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan], 'b': [np.nan, 2., np.nan, 6.], 'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.], 'b': [np.nan, 3., 4., 6., 8.]})
print(df2)
print(df1)
print(df1.combine_first(df2))