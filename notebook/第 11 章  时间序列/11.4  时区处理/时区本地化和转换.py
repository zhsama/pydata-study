# @Version : Python3.6
# @Time    : 2018/6/14 21:18
# @Author  : zhcf1ess
# @Site    : 
# @File    : 时区本地化和转换.py
# @Software: PyCharm
import pytz
import pandas as pd
import numpy as np

rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')  # 随机一个日期列表
# print(rng)
ts = pd.Series(np.random.randn(6), index=rng)
# print(ts)
# print(ts.index.tz)
tz = pd.date_range('3/9/2012 9:30', freq='D', periods=10, tz='UTC')
# print(tz)
# 本地化
ts_utc = ts.tz_localize('UTC')
# print(ts_utc)
ts_ny = ts_utc.tz_convert('America/New_York')
print(ts_ny)
print(ts.index.tz_localize('UTC'))