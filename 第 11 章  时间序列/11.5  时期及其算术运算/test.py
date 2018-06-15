# @Version : Python3.6
# @Time    : 2018/6/15 17:36
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pandas as pd
import numpy as np

p = pd.Period(2018, 'A-DEC')
# print(p)  # 这个Period对象表示的是从2007年1月1日到2007年12月31日之间的整段时间
p2 = pd.Period('2014', freq='A-DEC')
# print(p - p2)

rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
# print(rng)

ds = pd.Series(np.random.randn(6), index=rng)
print(ds)

values = ['2001Q3', '2002Q2', '2003Q1']
index = pd.PeriodIndex(values, freq='Q-DEC')
print(index)
