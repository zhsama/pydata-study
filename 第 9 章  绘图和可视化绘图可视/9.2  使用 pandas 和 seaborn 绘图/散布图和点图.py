# @Version : Python3.6
# @Time    : 2018/6/8 16:54
# @Author  : zhcf1ess
# @Site    : 
# @File    : 散布图和点图.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

macro = pd.read_csv('macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
# print(trans_data[-5:])

# regplot
# sns.regplot('m1', 'unemp', data=trans_data)
# plt.title('Changes in  log %s  versus  log %s' % ('m1', 'unemp'))
# plt.savefig('test.png', bbox_inches='tight')

# pairplot
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
plt.show()
