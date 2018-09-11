# @Version : Python3.6
# @Time    : 2018/6/8 16:53
# @Author  : zhcf1ess
# @Site    : 
# @File    : 分面网格（facet  grid）和类型数据.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv('tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts = party_counts.loc[:, 2:5]
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
# print(party_pcts)
# party_pcts.plot.bar()
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
# print(tips.head())

# sns.factorplot(x='day', y='tip_pct', hue='time', col='smoker', kind='bar', data=tips[tips.tip_pct < 1])
# 通过给每个时间值添加一行来扩展分面网格
# sns.factorplot(x='day', y='tip_pct', row='time', col='smoker', kind='bar', data=tips[tips.tip_pct < 1])

# 盒图 king=box
sns.factorplot(x='tip_pct', y='day', kind='box', data=tips[tips.tip_pct < 0.5])
plt.show()
