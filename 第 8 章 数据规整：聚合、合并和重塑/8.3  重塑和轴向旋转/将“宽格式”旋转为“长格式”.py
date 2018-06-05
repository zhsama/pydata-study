# @Version : Python3.6
# @Time    : 2018/6/5 18:46
# @Author  : zhcf1ess
# @Site    : 
# @File    : 将“宽格式”旋转为“长格式”.py
# @Software: PyCharm

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'key': ['foo', 'bar', 'baz'],
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})
# print(df)
melted = pd.melt(df, ['key'])
# print(pd.melt(df, 'key'))
pivoted = melted.pivot('key', 'variable', 'value')
# print(pivoted)
print(pivoted.reset_index())

# 指定列的子集作为值的列
print(pd.melt(df, id_vars=['key'], value_vars=['A', 'B']))

# 不用分组指标
print(pd.melt(df, value_vars=['A', 'B', 'C']))
print(pd.melt(df, value_vars=['key', 'A', 'B']))
