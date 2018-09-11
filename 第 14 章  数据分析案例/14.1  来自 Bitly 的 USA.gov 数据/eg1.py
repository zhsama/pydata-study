# @Version : Python3.6
# @Time    : 2018/9/10 19:49
# @Author  : zhcf1ess
# @Site    : 
# @File    : eg1.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

# 读取文件 转化为json格式
file = 'example.txt'
records = [json.loads(line) for line in open(file)]
# print(records[:3])

# 数据转化为DataFrame 然后清洗
frame = pd.DataFrame(records)
# print(frame.info())
# tz_count = frame['tz'].value_counts()
# print(tz_count[:10])
clean_tz = frame['tz'].fillna('missing')
clean_tz[clean_tz == ''] = 'unknown'
tz_count = clean_tz.value_counts()

# 对时区进行计数
# subset = tz_count[:10]
# sns.barplot(y=subset.index, x=subset.values)
# plt.show()

# 浏览用户的ua计数
# results = pd.Series([x.split()[0] for x in frame.a.dropna()])
# print(results[:5])
# print(results.value_counts()[:10])
# clean_ua = results
# ua_count = clean_ua.value_counts()[:3]
# print(ua_count[:10])
# sns.barplot(y=ua_count.index, x=ua_count.values)
# plt.show()

# 按Windows和非Windows用户对时区统计信息进行分解
cframe = frame[frame.a.notnull()]  # 筛选'a'字段非na的值
cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')  # 判断每行是否含有'windows'
# print(cframe['os'][:5])
by_tz_os = cframe.groupby(['tz', 'os'])
agg_counts = by_tz_os.size().unstack().fillna(0)  # 重塑DataFrame 行列互换 清除na
# print(agg_counts[:10])

# 构造简介索引数组
indexer = agg_counts.sum(1).argsort()  # 根据索引和值排序
# print(indexer[:10])

#
count_subset = agg_counts.take(indexer[-10:])  # 截取最后10行最大值
# print(count_subset)
# count_subset = agg_counts.sum(1).nlargest(10)  # sum(1)根据行求值 nlargest(10)降序排列 获取前十个数

# 绘图
count_subset = count_subset.stack()
# print(count_subset)
count_subset.name = 'total'
count_subset = count_subset.reset_index()
print(count_subset[:10])
# sns.barplot(x='total', y='tz', hue='os', data=count_subset)
# plt.show()