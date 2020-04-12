# @Version : Python3.6
# @Time    : 2018/6/17 19:24
# @Author  : zhcf1ess
# @Site    : 
# @File    : 分组的时间重采样.py
# @Software: PyCharm
import pandas as pd
import numpy as np

N = 15
times = pd.date_range('2017-05-20  00:00', freq='1min', periods=N)
df = pd.DataFrame({
    'times': times,
    'value': np.arange(N)
})
# print(df)
# print(df.set_index('times').resample('5min').count())


df2 = pd.DataFrame({
    'time': times.repeat(3),
    'key': np.tile(['a', 'b', 'c'], N),
    'value': np.arange(N * 3.)
})
# print(df2)

time_key = pd.TimeGrouper('5min')
resampled = (df2.set_index('time').groupby(['key', time_key]).sum())
print(resampled)
print(resampled.reset_index())