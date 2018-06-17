# @Version : Python3.6
# @Time    : 2018/6/17 19:05
# @Author  : zhcf1ess
# @Site    : 
# @File    : 分组转换和解封”GroupBy.py
# @Software: PyCharm
import pandas as pd
import numpy as np

df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4, 'value': np.arange(12.)})
# print(df)
g = df1 = df.groupby('key').value


# df2 = df.groupby('key')
# print(df1)
# print(df2)

# print(g.mean())
# print(g.transform(lambda x: x.mean()))
# print(g.transform('mean'))  # 类似agg的用法 传入一个函数名字符串
# print(g.transform(lambda x: x * 2))  # 返回一个series
# print(g.transform(lambda x: x.rank(ascending=False)))  # 由高到低排序

def normalize(x):
    return (x - x.mean()) / x.std()


print(g.transform(normalize))
print(g.apply(normalize))