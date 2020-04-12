# @Version : Python3.6
# @Time    : 2018/5/24 20:05
# @Author  : zhcf1ess
# @Site    : 
# @File    : 数组转置和轴对换.py
# @Software: PyCharm
# import numpy as np

# T
# arr = np.arange(15).reshape((3, 5))
# print(arr)
# print(arr.T) # 数组转置

# 计算矩阵内积
# arr = np.random.randn(6, 3)
# print(np.dot(arr.T, arr))

# transpose
# arr = np.arange(16).reshape((2, 2, 4))
# print(arr.transpose(1, 0, 2))# 把arr[0][1][2]变成arr[1][0][2]
# print(arr)

# swapaxes
arr = np.arange(16).reshape((2, 2, 4))
print(arr.swapaxes(1, 2))
