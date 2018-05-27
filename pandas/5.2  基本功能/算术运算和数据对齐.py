# @Version : Python3.6
# @Time    : 2018/5/27 20:17
# @Author  : zhcf1ess
# @Site    : 
# @File    : 算术运算和数据对齐.py
# @Software: PyCharm

import numpy as np
import pandas as pd

# s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
# s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

# print(s1 + s2) # 自动将相同索引的数值相加 不重叠的索引值设为nan
# 对于 DataFrame，对齐操作会同时发生在行和列上
f1 = pd.DataFrame(
    np.arange(9.).reshape((3, 3)),
    columns=list('bcd'),
    index=['Ohio', 'Texas', 'Colorado']
)

f2 = pd.DataFrame(
    np.arange(12.).reshape((4, 3)),
    columns=list('bde'),
    index=['Utah', 'Ohio', 'Texas', 'Oregon']
)
# print(f1 + f2)
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [1, 2]})
# print(df1+df2)