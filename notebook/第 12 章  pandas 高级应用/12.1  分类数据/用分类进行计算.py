# @Version : Python3.6
# @Time    : 2018/6/16 22:34
# @Author  : zhcf1ess
# @Site    : 
# @File    : 用分类进行计算.py
# @Software: PyCharm
import pandas as pd
import numpy as np

np.random.seed(1234)
draws = np.random.randn(1000)
print(draws)
bins = pd.qcut(draws, 4)
bins1 = pd.cut(draws, 4)
print(bins1)
# bins1 = pd.qcut(draws, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
# print(bins)
# print(bins1)

bins = pd.Series(bins, name='quartile')
bins = pd.Series(bins, name='quartile')
# print(bins)
results = (pd.Series(draws).groupby(bins).agg(['count', 'min', 'max']).reset_index())
# print(results)
# print(results['quartile'])
