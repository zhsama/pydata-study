# @Version : Python3.6
# @Time    : 2018/5/26 21:06
# @Author  : zhcf1ess
# @Site    : 
# @File    : Index.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

obj = pd.Series(range(3), index=['1', '2', '3'])
index = obj.index
# print(index)
# print(index[1])
# print(index[1:])

# 不可变(在不同数据结构中安全传递)
# try:
#     index[1] = 'a'
# except:
#     print('index标签不可变')

# 有序集合 可重复标签
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
# print(dup_labels)