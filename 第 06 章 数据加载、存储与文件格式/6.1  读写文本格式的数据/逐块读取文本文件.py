# @Version : Python3.6
# @Time    : 2018/5/30 18:29
# @Author  : zhcf1ess
# @Site    : 
# @File    : 逐块读取文本文件.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10
result = pd.read_csv('ex6.csv')
# print(result)

# 指定读取第x行
df = pd.read_csv('ex6.csv', nrows=5)
# print(df)

# 逐块读取文件
chunker = pd.read_csv('ex6.csv', chunksize=1000)  # chunker为textpaper可迭代对象 每1000分为一块
# print(chunker)

# 对某个索引出现次数进行排序
tot = pd.Series([])  # 设置一个空的series对象
for piece in chunker:
    # print(piece['key'])
    tot = tot.add(piece['key'].value_counts(), fill_value=0)  # 计算每个key出现频率 填入tot中
    # print(tot)
# print(tot.sort_values(ascending=False))  # 降序排列
# plt.plot(tot)
# plt.bar(tot)
labels = tot.index
print(labels)
# explode = tot.index[-1]
# print(explode)
# plt.pie(tot, labels=labels)
# plt.show()
