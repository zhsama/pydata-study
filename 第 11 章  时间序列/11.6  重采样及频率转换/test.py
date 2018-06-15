# @Version : Python3.6
# @Time    : 2018/6/15 20:41
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pandas as pd
import numpy as np

rng = pd.date_range('2000-01-01', periods=100, freq=' D')
# print(rng)
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts)
# print(ts.resample('M').mean())
print(ts.resample('M', kind='period').mean())  # 转换成时间段索引
