# @Version : Python3.6
# @Time    : 2018/6/15 20:57
# @Author  : zhcf1ess
# @Site    : 
# @File    : 降采样.py
# @Software: PyCharm
import pandas as pd
import numpy as np

rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts)
# print(ts.resample('5min', closed='right').sum())
# print(ts.resample('5min', closed='left').sum())
# print(ts.resample('5min', label='right').sum())
# print(ts.resample('5min', label='left').sum())
# print(ts.resample('5min', closed='left', label='right').sum())
# print(ts.resample('5min', closed='right', label='right').sum())

print(ts.resample('5min', closed='right', label='right', loffset='-1s').sum())  # 设置索引偏移量
