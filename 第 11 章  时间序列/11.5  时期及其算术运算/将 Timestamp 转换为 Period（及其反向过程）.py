# @Version : Python3.6
# @Time    : 2018/6/15 18:47
# @Author  : zhcf1ess
# @Site    : 
# @File    : 将 Timestamp 转换为 Period（及其反向过程）.py
# @Software: PyCharm
import pandas as pd
import numpy as np

rng = pd.date_range('2000-01-01', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)
# print(ts)
# print(ts.to_period())
ts_p = ts.to_period()
print(ts_p.to_timestamp())
