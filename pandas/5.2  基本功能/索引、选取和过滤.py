# @Version : Python3.6
# @Time    : 2018/5/27 17:20
# @Author  : zhcf1ess
# @Site    : 
# @File    : 索引、选取和过滤.py
# @Software: PyCharm

import numpy as np
import pandas as pd

obj = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])
# print(obj['a'])
# print(obj[1])

# 切片
# 利用标签切片包含末端
# print(obj['a':'b'])
# print(obj[1:2])

frame = pd.DataFrame(
    np.arange(16).reshape(4, 4),
    index=['Ohio', 'Colorado', 'Utah', 'NewYork'],
    columns=['one', 'two', 'three', 'four']
)
# 返回series对象
# print(frame['one'])
# print(frame.one)

# 返回dataframe对象
# print(frame[['one']])
# print(frame[['one','two']])

# 切片获取
# print(frame[:2])  # [0,2)前开后闭
# print(frame['three'] > 1)  # 布尔值获取
# frame2 = frame[frame < 5] = 0
# print(frame2)

# 通过行索引获取
# print(frame.ix['Ohio'])
