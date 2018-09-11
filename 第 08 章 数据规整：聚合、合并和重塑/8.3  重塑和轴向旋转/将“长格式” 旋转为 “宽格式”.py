# @Version : Python3.6
# @Time    : 2018/6/5 18:45
# @Author  : zhcf1ess
# @Site    : 
# @File    : 将“长格式” 旋转为 “宽格式”.py
# @Software: PyCharm
import pandas as pd
import numpy as np

data = pd.read_csv('macrodata.csv')
# print(data.head())

periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
# print(periods)

columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)  # 重排索引
# print(data)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})
# print(ldata)

# 使用指定的`index` /`columns`中的唯一值来形成生成的DataFrame的轴。
# pivoted = ldata.pivot('date', 'item', 'value')
# print(pivoted)