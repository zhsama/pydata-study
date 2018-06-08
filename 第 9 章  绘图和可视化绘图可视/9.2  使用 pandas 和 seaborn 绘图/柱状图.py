# @Version : Python3.6
# @Time    : 2018/6/8 15:50
# @Author  : zhcf1ess
# @Site    : 
# @File    : 柱状图.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 1)

# series
data = pd.Series(np.random.randn(16), index=list('abcdefghijklmnop'))
# print(data)
# data.value_counts().plot.bar(ax=axes[0], color='k', alpha=0.7)
# data.plot.barh(ax=axes[1], color='k', alpha=0.7)

# dataframe
df = pd.DataFrame(
    np.random.rand(6, 4),
    index=['one', 'two', 'three', 'four', 'five', 'six'],
    columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus')
)
print(df)
# df.plot.barh()
# df.plot.bar(stacked=True, alpha=0.7)
# plt.show()

tips = pd.read_csv('tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts = party_counts.loc[:, 2:5]
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
# print(party_pcts)
# party_pcts.plot.bar()
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
# print(tips.head())
sns.barplot(x='tip_pct', y='day', data=tips, orient='h')
plt.show()
