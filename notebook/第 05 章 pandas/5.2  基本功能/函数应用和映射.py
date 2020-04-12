# @Version : Python3.6
# @Time    : 2018/5/29 15:59
# @Author  : zhcf1ess
# @Site    : 
# @File    : 函数应用和映射.py
# @Software: PyCharm

import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(16).reshape(4, 4),
                     index=list('abcd'),
                     columns=list('wxyz'))
# print(frame)
frame1 = pd.DataFrame(
    np.random.randn(4, 3),
    columns=list('bde'),
    index=['Utah', 'Ohio', 'Texas', 'Oregon']
)
# print(frame1)
# print(np.abs(frame1))

# 将函数应用到由各列或行所形成的一维数组上
# 这里的函数 f，计算了一个 Series 的最大值和最小值的差，在 frame 的每列都执行了一次。
# 结果是一个 Series，使用 frame 的列作为索引
f = lambda x: x.max() - x.min()
# print(frame1.apply(f))

# 如果传递 axis='columns'到 apply，这个函数会在每行执行
# print(frame1.apply(f, axis='columns'))


# 向apply传递返回值为series的函数
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
# print(frame1.apply(f))