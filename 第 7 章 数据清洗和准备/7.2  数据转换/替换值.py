# @Version : Python3.6
# @Time    : 2018/6/1 19:51
# @Author  : zhcf1ess
# @Site    : 
# @File    : 替换值.py
# @Software: PyCharm

import pandas as pd
import numpy as np

data = pd.Series([1., -999., 2., -999., -1000., 3.])
# print(data)
print(data.replace(-999, np.nan))
# 传入列表
print(data.replace([-999, -1000], np.nan))
# 传入替换列表
print(data.replace([-999, -1000], [np.nan, 0]))
print(data.replace({-999: np.nan, -1000: 0}))  # 传入字典修改 等价与上式
