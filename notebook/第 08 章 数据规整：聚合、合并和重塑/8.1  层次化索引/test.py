# @Version : Python3.6
# @Time    : 2018/6/3 10:59
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import numpy as np
import pandas as pd
# from pandas import MultiIndex
from pandas import MultiIndex

data = pd.Series(
    np.random.randn(9),
    index=[
        ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
        [1, 2, 3, 1, 3, 1, 2, 2, 3]
    ]
)
# print(data)
# print(data.index)

# 选取子集
# print(data.b)
# print(data.c)
# print(data['b':'c'])

# loc iloc
# print(data.loc[:, [1, 2]])
# print(data.iloc[2:1])

# stack unstack
# print(data.unstack())
df = data.unstack()
# print(df.stack())


frame = pd.DataFrame(
    np.arange(12).reshape((4, 3)),
    index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
    columns=[
        ['Ohio', 'Ohio', 'Colora do'],
        ['Green', 'Red', 'Green']
    ]
)
# print(frame)
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
# print(frame)

# print(frame.Ohio)
#
# print(MultiIndex.from_arrays(
#         [
#             ['Ohio', 'Ohio', 'Colorado'],
#             ['Green', 'Red', 'Green']
#         ],
#         names=['state', 'color']
#     )
# )
