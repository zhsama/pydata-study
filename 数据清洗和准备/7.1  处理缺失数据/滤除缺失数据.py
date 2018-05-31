# @Version : Python3.6
# @Time    : 2018/5/31 20:17
# @Author  : zhcf1ess
# @Site    : 
# @File    : 滤除缺失数据.py
# @Software: PyCharm

import pandas as pd
import numpy as np
from numpy import nan as na

data = pd.Series([1, na, 3.5, na, 7])
# print(data.dropna())  # 清除所有na值
# print(data[data.notnull()])  # 等价

# dataframe
data = pd.DataFrame([[1., 6.5, 3.], [1., na, na], [na, na, na], [na, 6.5, 3.]])
# print(data)
print(data.dropna())