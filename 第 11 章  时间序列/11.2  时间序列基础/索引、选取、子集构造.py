# @Version : Python3.6
# @Time    : 2018/6/14 19:43
# @Author  : zhcf1ess
# @Site    : 
# @File    : 索引、选取、子集构造.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from datetime import datetime

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)

stamp = ts.index[2]
# print(ts[stamp])

longer_ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# print(longer_ts['2001'])
# print(longer_ts['2001-01'])
# print(ts[datetime(2011, 1, 7):])

# print(ts['1/6/2011':'1/11/2011'])
# print(ts.truncate(after='1/9/2011'))  # 在某个索引值之前和之后截断一个Series或DataFrame。

dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4), index=dates, columns=['Colorado', 'Texas', 'New  York', 'Ohio'])
print(long_df['1-2001'])
