# @Version : Python3.6
# @Time    : 2018/6/3 10:59
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import numpy as np
import pandas as pd

data = pd.Series(
    np.random.randn(9),
    index=[
        ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
        [1, 2, 3, 1, 3, 1, 2, 2, 3]
    ]
)
print(data)
print(data.index)