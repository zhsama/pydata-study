# @Version : Python3.6
# @Time    : 2018/5/29 16:49
# @Author  : zhcf1ess
# @Site    : 
# @File    : 排序和排名.py
# @Software: PyCharm

import numpy as np
import pandas as pd

# series
# obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
# print(obj)
# print(obj.sort_index())  # 按索引标签排序系列。

# dataframe
frame = pd.DataFrame(
    np.arange(8).reshape((2, 4)),
    index=['three', 'one'],
    columns=['d', 'a', 'b', 'c']
)
# print(frame)
# print(frame.sort_index)
# print(frame.sort_index(axis=0))
# print(frame.sort_index(axis=1, ascending=False))

obj = pd.Series([4, 7, -3, 2])
# print(obj.sort_values())

frame1 = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
# print(frame1.sort_values(by='b')) # 只对b进行拍序
# print(frame1.sort_values(by=['a', 'b'])) # 对a，b进行拍序

# 乱序
# print(obj.rank())
# print(obj.rank(method='first'))
print(frame.rank(axis='columns'))
