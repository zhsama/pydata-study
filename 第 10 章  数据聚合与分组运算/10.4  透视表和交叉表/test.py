# @Version : Python3.6
# @Time    : 2018/6/9 18:03
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pandas as pd
import numpy as np

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

# print(tips.pivot_table(index=['day', 'smoker']))
# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker'))
# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True))
# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True, aggfunc=len))
# print(tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'], columns='smoker', margins=True, aggfunc=len,
                       # fill_value=0))