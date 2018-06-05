# @Version : Python3.6
# @Time    : 2018/5/25 20:37
# @Author  : zhcf1ess
# @Site    : 
# @File    : 排序.py
# @Software: PyCharm

import numpy as np

# arr = np.random.randn(6)
# arr = np.random.randn(5, 3)
# print(arr)
# print(arr.sort())
# print(arr.sort(1))
large_arr = np.random.randn(1000)
# print(large_arr)
large_arr.sort()
large_arr[int(0.05 * len(large_arr))]
print(np.percentile(large_arr, 5))
