# @Version : Python3.6
# @Time    : 2018/6/14 20:08
# @Author  : zhcf1ess
# @Site    : 
# @File    : 带有重复索引的时间序列.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from datetime import datetime

dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.random.randn(5), index=dates)
# print(dup_ts)
print(dup_ts.index.is_unique)  # 判断index是否重复
print(dup_ts['1/3/2000'])  # 不重复
print(dup_ts['1/2/2000'])  # 重复
