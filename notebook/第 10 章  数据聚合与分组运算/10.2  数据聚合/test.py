# @Version : Python3.6
# @Time    : 2018/6/9 16:11
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'key1': ['a', 'a', 'b', 'b', 'a'],
        'key2': ['one', 'two', 'one', 'two ', 'one'],
        'data1': np.random.randn(5),
        'data2': np.random.randn(5)
    }
)
grouped = df.groupby('key1')


# print(grouped['data1'].quantile(0.9))

def peak_to_peak(arr):
    return arr.max() - arr.min()
print(grouped.agg(peak_to_peak))