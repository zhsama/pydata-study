# @Version : Python3.6
# @Time    : 2018/6/15 18:00
# @Author  : zhcf1ess
# @Site    : 
# @File    : 时期的频率转换.py
# @Software: PyCharm
import pandas as pd
import numpy as np

p = pd.Period('2007', freq='A-DEC')
# print(p)
# print(p.asfreq('M', how='start'))
# print(p.asfreq('M', how='end'))

rng = pd.period_range('2006', '2009', freq='A-DEC')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts)
# print(ts.asfreq('M', how='start'))
# print(ts.asfreq('B', how='end'))

p = pd.Period('Aug-2007', 'M')
# print(p)
# print(p.asfreq('A-JUN'))
