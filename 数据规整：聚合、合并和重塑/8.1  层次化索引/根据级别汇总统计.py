# @Version : Python3.6
# @Time    : 2018/6/3 16:24
# @Author  : zhcf1ess
# @Site    : 
# @File    : 根据级别汇总统计.py
# @Software: PyCharm
import numpy as np
import pandas as pd

frame = pd.DataFrame(
    np.arange(12).reshape((4, 3)),
    index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2], ['c', 'd', 'd', 'c']],
    columns=[
        ['Ohio', 'Ohio', 'Colorado'],
        ['Green', 'Red', 'Green']
    ]
)
frame.index.names = ['key1', 'key2', 'key3']
frame.columns.names = ['state', 'color']
print(frame)

print(frame.sum(level=0))
print(frame.sum(level=0, axis=1))
