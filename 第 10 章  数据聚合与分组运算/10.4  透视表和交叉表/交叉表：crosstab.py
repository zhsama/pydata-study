# @Version : Python3.6
# @Time    : 2018/6/9 18:03
# @Author  : zhcf1ess
# @Site    : 
# @File    : 交叉表：crosstab.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
# group_key = ['East'] * 4 + ['West'] * 4
# data = pd.Series(np.random.randn(8), index=states)
# print(data)

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(pd.crosstab([tips.day, tips.time], tips.smoker, margins=True))  # 计算分组频率
