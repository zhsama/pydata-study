# @Version : Python3.6
# @Time    : 2018/6/9 15:43
# @Author  : zhcf1ess
# @Site    : 
# @File    : 通过函数进行分组.py
# @Software: PyCharm
import pandas as pd
import numpy as np

people = pd.DataFrame(
    np.random.randn(5, 5),
    columns=['a', 'b', 'c', 'd', 'e'],
    index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis']
)
# 根据人名长度分组
# print(people.groupby(len).mean())
print(people.groupby(len, axis=1).mean())

# 混用
# key_list = ['one', 'one', 'one', 'two', 'two']
# print(people.groupby(len, key_list).min())
