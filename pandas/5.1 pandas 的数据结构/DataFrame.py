# @Version : Python3.6
# @Time    : 2018/5/26 18:56
# @Author  : zhcf1ess
# @Site    : 
# @File    : DataFrame.py
# @Software: PyCharm

import pandas as pd

data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}
frame = pd.DataFrame(data)
# print(frame)

# 产生缺省值
# columns设置列名
# index设置列索引
frame2 = pd.DataFrame(
    data,
    columns=['year', 'state', 'pop', 'debt'],
    index=['one', 'two', 'three', 'four', 'five', 'six']
)

# print(frame2)

# 指定列序列
# print(pd.DataFrame(data, columns=['pop', 'state', 'year']))


#  DataFrame 的列获取为一个 Series
# frame2[column]适用于任何列的名
# frame2.column 只有在列名是一个合理的 Python 变量名时才适用
# print(frame2['state'])
# print(frame2.state)

# 获取行
# print(frame2.loc['three'])

# 设置列
# frame2['debt'] = 666
# print(frame2)
# import numpy as  np
#
# frame2['debt'] = np.arange(6)
# print(frame2)

# 传入Series可以匹配索引index
# val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# frame2['debt'] = val
# print(frame2)

# del删除对应行(列)
# frame2['bool'] = frame2['state'] == 'Ohio'
# print(frame2)
# del frame2['bool']
# print(frame2)

# 嵌套字典
pop = {
    'Nevada': {2001: 2.4, 2002: 2.9},
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
}
frame3 = pd.DataFrame(pop)
# print(frame3)
# print(frame3.Ohio)

# 转置dataframe
# print(frame3.T)

# 合并索引
# print(pd.DataFrame(pop, index=[2001, 2002, 2003]))