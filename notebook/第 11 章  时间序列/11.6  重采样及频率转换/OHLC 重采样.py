# @Version : Python3.6
# @Time    : 2018/6/15 21:13
# @Author  : zhcf1ess
# @Site    : 
# @File    : OHLC 重采样.py
# @Software: PyCharm
import pandas as pd
import numpy as np


rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts.resample('5min').ohlc())