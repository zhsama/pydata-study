# @Version : Python3.6
# @Time    : 2018/6/1 16:59
# @Author  : zhcf1ess
# @Site    : 
# @File    : 移除重复数据.py
# @Software: PyCharm

import numpy as np
import pandas as pd
from numpy import nan as na

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
# print(data.duplicated())
# print(data.drop_duplicates())

data['v1'] = range(7)
# print(data)
print(data.drop_duplicates(['k1']))
print(data.drop_duplicates(['k1'], keep='last'))
