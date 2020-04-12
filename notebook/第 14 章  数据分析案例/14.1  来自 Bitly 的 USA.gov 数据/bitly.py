# @Version : Python3.6
# @Time    : 2018/9/11 19:46
# @Author  : zhcf1ess
# @Site    : 
# @File    : bitly.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

# 将文件读取成json格式
file = open('example.txt')
records = [json.loads(line) for line in file]
# print(records)

# 对文件中的数据进行清洗
frame = pd.DataFrame(records)
cframe = frame[frame.a.notnull()]
# print(cframe.a[:5])
cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', 'os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
# print(agg_counts)

# 对os字段权重重排序
index = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(index[-10:])
# print(count_subset)

#
result = count_subset.stack()
# print(result)
result.name = "total"
result = result.reset_index()
# print(result)

# 绘图
sns.barplot(x='total', y='tz', hue='os', data=result)
plt.show()
