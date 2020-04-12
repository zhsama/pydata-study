# @Version : Python3.6
# @Time    : 2018/6/14 21:19
# @Author  : zhcf1ess
# @Site    : 
# @File    : 不同时区之间的运算.py
# @Software: PyCharm
import pytz
import pandas as pd
import numpy as np

rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts1 = ts[:7].tz_localize('Europe/London')
ts2 = ts1[2:].tz_convert('Europe/Moscow')
print(ts1 + ts2)
