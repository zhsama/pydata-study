# @Version : Python3.6
# @Time    : 2018/6/9 16:43
# @Author  : zhcf1ess
# @Site    : 
# @File    : 以“没有行索引”的形式返回聚合数据.py
# @Software: PyCharm
import pandas as pd
import numpy as np


tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

print(tips.groupby(['day', 'smoker'], as_index=False).mean())
print(tips.groupby(['day', 'smoker']).mean())