# @Version : Python3.6
# @Time    : 2018/6/9 16:49
# @Author  : zhcf1ess
# @Site    : 
# @File    : 禁止分组键.py
# @Software: PyCharm
import pandas as pd
import numpy as np

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

# print(tips.groupby('smoker', group_keys=False).apply(max))
# print(tips.groupby('smoker', as_index=False).apply(sum))
# print(tips.groupby('smoker').apply(max))

