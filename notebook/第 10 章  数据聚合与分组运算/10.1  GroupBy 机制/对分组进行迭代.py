# @Version : Python3.6
# @Time    : 2018/6/8 20:47
# @Author  : zhcf1ess
# @Site    : 
# @File    : 对分组进行迭代.py
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

# GroupBy 对象支持迭代，可以产生一组二元元组（由分组名和数据块组成）
# for name, group in df.groupby('key1'):
#     print(name)
#     print(group)

# 对于多重键的情况，元组的第一个元素将会是由键值组成的元组
# for (k1, k2), group in df.groupby(['key1', 'key2']):
#     print((k1, k2))
#     print(group)

# 转换成字典
pieces = dict(list(df.groupby('key1')))
print(pieces)

# 默认axis=0 可重设
grouped = df.groupby(df.dtypes, axis=1)
for  dtype,  group  in  grouped: 
    print(dtype)  
    print(group)  