# @Version : Python3.6
# @Time    : 2018/6/5 18:44
# @Author  : zhcf1ess
# @Site    : 
# @File    : 重塑层次化索引.py
# @Software: PyCharm
import numpy as np
import pandas as pd

data = pd.DataFrame(
    np.arange(6).reshape((2, 3)),
    index=pd.Index(['Ohio', 'Colorado'], name='state'),
    columns=pd.Index(['one', 'two', 'three'], name='number')
)
print(data)
res = data.stack()
print(res)
# print(res.unstack())
# 操作指定层的索引
# print(res.unstack(0))
# print(res.unstack('state'))  # 通过索引ｎａｍｅ操作

# 产生/消除 nan值
s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd '])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
# print(s1, s2)
# data2 = pd.concat([s1, s2], keys=['one', 'two'])
# print(data2.unstack())
# print(data2.unstack().stack())

# 
df = pd.DataFrame(
    {'left': res, 'right': res + 5},
    columns=pd.Index(['left', 'right'], name='side')
)
print(df)
# print(df.unstack())
# print(df.unstack('state'))
print(df.unstack('state').stack('side'))
