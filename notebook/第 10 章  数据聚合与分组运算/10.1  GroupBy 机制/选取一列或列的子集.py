# @Version : Python3.6
# @Time    : 2018/6/8 21:03
# @Author  : zhcf1ess
# @Site    : 
# @File    : 选取一列或列的子集.py
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
# print(df.groupby('key1')['data1'].size())
# print(df['data1'].groupby(df['key1']).size())

# print(df.groupby(['key1','key2'])['data1'].mean())
print(df['data1'].groupby([df['key1'], df['key2']]).mean())
