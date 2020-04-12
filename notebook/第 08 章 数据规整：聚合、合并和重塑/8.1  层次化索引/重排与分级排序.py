# @Version : Python3.6
# @Time    : 2018/6/3 11:54
# @Author  : zhcf1ess
# @Site    : 
# @File    : 重排与分级排序.py
# @Software: PyCharm
import pandas as pd
import numpy as np

frame = pd.DataFrame(
    np.arange(12).reshape((4, 3)),
    index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2], ['c', 'd', 'd', 'c']],
    columns=[
        ['Ohio', 'Ohio', 'Colora do'],
        ['Green', 'Red', 'Green']
    ]
)
frame.index.names = ['key1', 'key2', 'key3']
frame.columns.names = ['state', 'color']
print(frame)
# print(frame.swaplevel('key1', 'key2'))

# print(frame.sort_index(level=0))
# print(frame.sort_index(level=1))
# print(frame.sort_index(level=2))

