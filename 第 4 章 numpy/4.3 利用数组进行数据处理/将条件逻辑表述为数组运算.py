# @Version : Python3.6
# @Time    : 2018/5/25 19:39
# @Author  : zhcf1ess
# @Site    : 
# @File    : 将条件逻辑表述为数组运算.py
# @Software: PyCharm
import numpy as np

# 传统python三元运算符
# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
# cond = np.array([True, False, True, True, False])
# result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
# print(result)

# where函数处理
# result = np.where(cond, xarr, yarr)
# print(result)

# 根据一个数组产生另一个数组
arr = np.random.randn(4, 4)
# print(arr)
# print(arr > 0)
# print(np.where(arr > 0, 2, -2))  # 大于0的数字替换成2 小于0的数字替换成-2
print(np.where(arr > 0, 2, arr))# 标量和适量结合用法
