# @Version : Python3.6
# @Time    : 2018/6/9 15:37
# @Author  : zhcf1ess
# @Site    : 
# @File    : 通过字典或 Series 进行分组.py
# @Software: PyCharm
import pandas as pd
import numpy as np

people = pd.DataFrame(
    np.random.randn(5, 5),
    columns=['a', 'b', 'c', 'd', 'e'],
    index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis']
)
people.iloc[2:3, [1, 2]] = np.nan

mapping = {
    'a': 'red', 'b': 'red', 'c': 'blue',
    'd': 'blue', 'e': 'red', 'f': 'orange'
}
# print(people.groupby(mapping, axis=1))

map_series = pd.Series(mapping)
# print(map_series)
print(people.groupby(map_series, axis=1).count())
