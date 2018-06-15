# @Version : Python3.6
# @Time    : 2018/6/14 21:19
# @Author  : zhcf1ess
# @Site    : 
# @File    : 操作时区意识型 Timestamp 对象.py
# @Software: PyCharm
import pytz
import pandas as pd
import numpy as np
from pandas.tseries.offsets import Hour

stamp = pd.Timestamp('2018-03-15  04:00')
# print(stamp)
stamp_utc = stamp.tz_localize("UTC")
# print(stamp_utc)
stamp_cg = stamp_utc.tz_convert('America/New_York')
# print(stamp_cg)

new_stamp = pd.Timestamp('2018-03-15  04:00', tz='Europe/Moscow')
# print(new_stamp)
# print(stamp.value)

stamp = pd.Timestamp('2012-03-12  01:30', tz='US/Eastern')
# print(stamp)
# print(stamp + Hour())
# print(stamp + 2 * Hour())
