# @Version : Python3.6
# @Time    : 2018/6/14 20:34
# @Author  : zhcf1ess
# @Site    : 
# @File    : 频率和日期偏移量.py
# @Software: PyCharm
from pandas.tseries.offsets import Hour, Minute
import pandas as pd
import numpy as np
from datetime import datetime

# 偏移量为4h
print(pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4h'))
print(pd.date_range('2000-01-01', '2000-01-03 23:59', freq='1h30min'))
