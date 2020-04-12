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


# 基本的索引和切片基本的索引和切片
# arr = np.arange(10)  # 类似range 返回数组对象
# print(arr)
# print(arr[0])
# print(arr[0:3])
# arr[5:8] = 12
# print(arr)
# arrc_copy = arr[5:8]
# arrc_copy[-1] = 0
# print(arrc_copy)
# print(arr)

# 复制数组
# arr_copy = arr[5:8].copy()
# print(arr_copy)
# arr_copy[-1] = 0
# print(arr_copy)
# print(arr)

# 二维数组
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2d[0][0])
# print(arr2d[0, 0])

# 三维数组
# arr3d = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])
# print(arr3d)
# print(arr3d[0])
# print(arr3d[0, 0])
# print(arr3d[0, 0, 0])
# arr = arr3d[0].copy()
# arr3d[1] = arr
# print(arr3d)

# 布尔型索引
# names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# data = np.random.randn(7, 4)
# print(names)
# print(data)
# print(names == 'Bob')
# print(data[names == 'Bob'])
# 布尔型数组的长度必须跟被索引的轴长度一致
# ~取反
# print(~(names == 'Bob'))
# print(data[~(names == 'Bob'), 3])

