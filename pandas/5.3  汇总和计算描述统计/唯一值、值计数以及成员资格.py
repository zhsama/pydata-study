# @Version : Python3.6
# @Time    : 2018/5/29 19:56
# @Author  : zhcf1ess
# @Site    : 
# @File    : 唯一值、值计数以及成员资格.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# print(obj)
# print(obj.unique())
# uniques = obj.unique()
# print(uniques.sort())
# print(obj.value_counts())

# value_counts是顶级方法
# print(pd.value_counts(obj.values, sort=False))
musk = obj.isin(['b', 'c'])
# print(musk)
# print(obj[musk])

# Index.get_indexer
# to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
# unique_vals = pd.Series(['a', 'b', 'c'])
# print(pd.Index(unique_vals).get_indexer(to_match))

data = pd.DataFrame({
    'Qu1': [1, 3, 4, 3, 4],
    'Qu2': [2, 3, 1, 2, 3],
    'Qu3': [1, 5, 2, 4, 4]
})
# print(data)
data_counts = data.apply(pd.value_counts).fillna(0)  # 计算频率 用0代替na值
# print(data_counts)
# plt.plot(data_counts)
# plt.show()