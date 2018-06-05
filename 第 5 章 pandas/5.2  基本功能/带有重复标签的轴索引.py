# @Version : Python3.6
# @Time    : 2018/5/29 17:30
# @Author  : zhcf1ess
# @Site    : 
# @File    : 带有重复标签的轴索引.py
# @Software: PyCharm

import numpy as np
import pandas as pd

frame = pd.DataFrame({
    'b': [4.3, 7, -3, 2],
    'a': [0, 1, 0, 1],
    'c': [-2, 5, 8, -2.5]
})

obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj.is_unique)

