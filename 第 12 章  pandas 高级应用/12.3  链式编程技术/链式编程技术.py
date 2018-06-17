# @Version : Python3.6
# @Time    : 2018/6/17 19:42
# @Author  : zhcf1ess
# @Site    : 
# @File    : 链式编程技术.py
# @Software: PyCharm
import pandas as pd
import numpy as np

df = load_data()
df2 = df[df['col2'] < 0]
df2['col1_demeaned'] = df2['col1'] - df2['col1'].mean()

df2 = df.copy()
df2['k'] = v
#  Functional  assign  way
df2 = df.assign(k=v)

result = df2.groupby('key').col1_demeaned.std()
result = (df2.assign(col1_demeaned=df2.col1 - df2.col2.mean()).groupby('key').col1_demeaned.std())
