# @Version : Python3.6
# @Time    : 2018/6/16 21:50
# @Author  : zhcf1ess
# @Site    : 
# @File    : 背景和目的.py
# @Software: PyCharm
import numpy as np
import pandas as pd

# values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
# print(values)
# print(pd.unique(values))
# print(pd.value_counts(values))

values = pd.Series([0, 1, 0, 0] * 2)
dim = pd.Series(['apple', 'orange'])

print(values)
print(dim)
print(dim.take(values))