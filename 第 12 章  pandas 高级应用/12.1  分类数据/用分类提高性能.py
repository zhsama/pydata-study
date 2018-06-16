# @Version : Python3.6
# @Time    : 2018/6/16 23:25
# @Author  : zhcf1ess
# @Site    : 
# @File    : 用分类提高性能.py
# @Software: PyCharm
import pandas as pd
import numpy as np

N = 10000000
draws = pd.Series(np.random.randn(N))
labels = pd.Series(['foo', 'bar', 'baz', 'qux'] * (N // 4))

categories = labels.astype('category')
# print(labels.memory_usage())
# print(categories.memory_usage())
print(categories)
print(labels)
