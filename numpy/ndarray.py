# @Version : Python3.6
# @Time    : 2018/5/23 20:36
# @Author  : zhcf1ess
# @Site    : 
# @File    : ndarray.py
# @Software: PyCharm

import numpy as np

# data = np.random.randn(2, 3)  # 从标准正态分布中返回一个或多个样本值
# print(data)
# print(type(data))
# print(data * 10)
# print(data + data)
# print(data.dtype)  # 说明数组数据类型的对象
# print(data.shape)  # 表示各维度大小的元组

# 创建数组
# data1 = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
# arr = np.array(data1)
# print(arr)

# data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
# arr2 = np.array(data2)
# # print(arr2)
# print(arr2.ndim)  # 查看数据有几维
# print(arr2.shape)  # 数组维度的元组

# arange  Python 内置函数 range 的数组版
# print(np.arange(10))

# ndarray 的数据类型
# arr1 = np.array([1, 2, 3], dtype=np.float64)
# arr2 = np.array([1, 2, 3, ], dtype=np.int32)
# print(arr2.dtype, arr1.dtype)

# astype更改数据类型
# arr = np.array([1, 2, 3, 4, 5])
# print(arr.dtype)
#
# change_type = arr.astype(np.float64)
# print(change_type.dtype)

# strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
# print(strings.astype(float))  # 可将全时数字的字符串转换成数字

# 数组运算
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# arr += arr
# print(arr)
# arr *= arr
# print(arr)

# 大小相同的数组之间的比较会生成布尔值数组
# arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
# print(arr2<arr)
# 三元运算符
# a,b=1,2
# max = (a if a > b else b)
# max = (a > b and [a] or [b])[0] #list
# max = (a > b and a or b)

