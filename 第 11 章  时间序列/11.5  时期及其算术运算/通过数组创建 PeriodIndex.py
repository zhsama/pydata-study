# @Version : Python3.6
# @Time    : 2018/6/15 18:54
# @Author  : zhcf1ess
# @Site    : 
# @File    : 通过数组创建 PeriodIndex.py
# @Software: PyCharm
import pandas as pd
import numpy as np

macro = pd.read_csv('macrodata.csv')
# print(macro.head())

index = pd.PeriodIndex(year=macro.year, quarter=macro.quarter, freq='Q-DEC')
# ds = pd.Series(np.random.randn(),index=index)
# print(index)
macro.index = index
print(macro.infl)
