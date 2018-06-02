# @Version : Python3.6
# @Time    : 2018/6/1 19:50
# @Author  : zhcf1ess
# @Site    : 
# @File    : 重命名轴索引.py
# @Software: PyCharm

import numpy as np
import pandas as pd

# print(data)
data = pd.DataFrame(
    np.arange(12).reshape((3, 4)),
    index=['Ohio', 'Colorado', 'New York'],
    columns=['one', 'two', 'three', 'four']
)

# transform = lambda x: x[:4].upper()  # 取前四个值进行大写转换
# print(data.index.map(transform))
# print(data.index)

# 在原对象上进行修改
# data.index = data.index.map(transform)
# print(data)

#
# print(data.rename(index=str.title, columns=str.upper))

# 传入字典对部分标签进行修改
# print(data.rename(index={'Ohio': 'INDIANA'}, columns={'three': 'peekaboo'}))
