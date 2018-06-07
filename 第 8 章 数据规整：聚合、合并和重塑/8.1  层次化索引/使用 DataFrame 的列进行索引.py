# @Version : Python3.6
# @Time    : 2018/6/3 16:34
# @Author  : zhcf1ess
# @Site    : 
# @File    : 使用 DataFrame 的列进行索引.py
# @Software: PyCharm
import numpy as np
import pandas as pd

frame = pd.DataFrame(
    {
        'a': range(7), 'b': range(7, 0, -1),
        'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
        'd': [0, 1, 2, 0, 1, 2, 3]
    }
)
# print(frame)
frame2 = frame.set_index(['c', 'd'])
print(frame2)
# print(frame2.index)
# print(frame2.index.names)
# print(frame2.swaplevel('c', 'd'))
#
# print(frame2.sort_index(level=1))

# 保留被设为levels的列索引
# print(frame.set_index(['c', 'd'], drop=False))

# reset_index()
print(frame2.reset_index())
