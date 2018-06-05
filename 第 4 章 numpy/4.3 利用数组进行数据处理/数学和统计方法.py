# @Version : Python3.6
# @Time    : 2018/5/25 19:48
# @Author  : zhcf1ess
# @Site    : 
# @File    : 数学和统计方法.py
# @Software: PyCharm

import numpy as np

# 聚合方法
# arr = np.random.randn(5, 4)
# print(arr)
# print(arr.mean())
# print(arr.sum())
# print(arr.mean(axis=1))
# print(arr.sum(axis=0))

# 不聚合方法
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
# print(arr.cumsum())  # 累加函数

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(arr)
# print(arr.cumsum(axis=1))
print(arr.cumprod(axis=0))
