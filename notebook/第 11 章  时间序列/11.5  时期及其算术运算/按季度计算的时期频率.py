# @Version : Python3.6
# @Time    : 2018/6/15 18:21
# @Author  : zhcf1ess
# @Site    : 
# @File    : 按季度计算的时期频率.py
# @Software: PyCharm
import pandas as pd
import numpy as np

p = pd.Period('2017Q4')
# print(p)
# p1 = p.asfreq('D', 'start')
# print(p1)
# p.asfreq('B', 'e')  # 第四个季度最后一个工作日
# print((p.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60)

rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
ds = pd.Series(np.random.randn(6), index=rng)
print(ds)
