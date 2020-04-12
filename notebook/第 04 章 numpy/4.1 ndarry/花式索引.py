# @Version : Python3.6
# @Time    : 2018/5/24 19:48
# @Author  : zhcf1ess
# @Site    : 
# @File    : 花式索引.py
# @Software: PyCharm
import numpy as np

# arr = np.empty((8, 4))
#
# for i in range(8):
#     arr[i] = i
#
# print(arr)
# print(arr[[5, 3, 7, 1]])

arr = np.arange(32).reshape(8, 4)  # 创建0~31的8列4行二位数组
# print(arr)
print(arr[[0, 3, 6, 1], [2, 1, 3, 0]])
# 打印【0，2】【3，1】。。。
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
