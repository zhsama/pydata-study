# @Version : Python3.6
# @Time    : 2018/6/15 21:30
# @Author  : zhcf1ess
# @Site    : 
# @File    : 升采样和插值.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# rng = pd.date_range('2000-01-01', periods=12, freq='T')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)

frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio']
                     )
# print(frame)
df_daily = frame.resample('D').asfreq()
# print(df_daily)
# print(frame.resample('D').ffill())
# print(frame.resample('D').ffill(limit=1))

#  新的日期索引完全没必要跟旧的重叠
print(frame.resample('W-THU').ffill())