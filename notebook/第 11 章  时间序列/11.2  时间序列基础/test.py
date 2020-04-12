# @Version : Python3.6
# @Time    : 2018/6/14 19:34
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from datetime import datetime
import pandas as pd
import numpy as np

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
# print(ts)

# print(ts.index)

# print(ts + ts[::2])

# print(ts.index.dtype)

# print(type(ts.index[0]))
