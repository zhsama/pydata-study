# @Version : Python3.6
# @Time    : 2018/6/14 20:56
# @Author  : zhcf1ess
# @Site    : 
# @File    : 通过偏移量对日期进行位移.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from datetime import datetime
from pandas.tseries.offsets import Day, MonthEnd

now = datetime(2018, 6, 14)
# print(now)
# print(now + MonthEnd())  # 增加量=目标时间-当前时间
# print(MonthEnd().rollforward(now))  # 后滚时间
# print(MonthEnd().rollback(now))  # 前滚时间

ts = pd.Series(np.random.randn(20), index=pd.date_range('1/15/2000', periods=20, freq='4d'))
# print(ts)
# print(ts.groupby(MonthEnd().rollforward.mean()))  # 每个月月末时间分类
print(ts.resample('M').mean())
