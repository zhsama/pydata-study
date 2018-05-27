# @Version : Python3.6
# @Time    : 2018/5/27 18:07
# @Author  : zhcf1ess
# @Site    : 
# @File    : 用 loc 和 iloc 进行选取.py
# @Software: PyCharm

import pandas as pd
import numpy as np

frame = pd.DataFrame(
    np.arange(16).reshape(4, 4),
    index=['Ohio', 'Colorado', 'Utah', 'NewYork'],
    columns=['one', 'two', 'three', 'four']
)
print(frame)
# print(frame.loc['Ohio', ['one', 'two']])  # 行索引 一行两列 返回series对象
# print(type(frame.iloc[1, [3, 0, 1]])) # 行索引 一行三列 返回series对象
