# @Version : Python3.6
# @Time    : 2018/6/8 16:06
# @Author  : zhcf1ess
# @Site    : 
# @File    : 直方图和密度图.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv('tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts = party_counts.loc[:, 2:5]
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])

# tips['tip_pct'].plot.hist(bins=50)
# tips['tip_pct'].plot.kde()
# tips['tip_pct'].plot.density()

comp1 = np.random.normal(0, 1, size=200)
comp2 = np.random.normal(10, 2, size=200)
values = pd.Series(np.concatenate([comp1, comp2]))
sns.distplot(values, bins=100, color='b', rug=True)
plt.show()
