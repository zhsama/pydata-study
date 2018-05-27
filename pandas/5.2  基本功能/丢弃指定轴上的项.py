# @Version : Python3.6
# @Time    : 2018/5/27 16:49
# @Author  : zhcf1ess
# @Site    : 
# @File    : 丢弃指定轴上的项.py
# @Software: PyCharm

import pandas as pd
import numpy as np

# series对象
obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
# print(obj)
# print(obj.drop('a'))

# inplace 删除原数组 不返回新对象 销毁被删除数据
obj.drop('a',inplace=True)
print(obj)

# DataFrame对象
frame = pd.DataFrame(
    np.arange(16).reshape(4, 4),
    index=['Ohio', 'Colorado', 'Utah', 'NewYork'],
    columns=['one', 'two', 'three', 'four']
)
# print(frame)
# print(frame.drop(index=['Ohio']))
# print(frame.drop(columns=['one']))
