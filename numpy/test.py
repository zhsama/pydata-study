# @Version : Python3.6
# @Time    : 2018/5/23 18:26
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import numpy as np

arr = np.arange(1000000)
lst = list(range(1000000))
# print(lst)
# print(arr)
for _ in range(10):
    lst2 = [x * 2 for x in lst]

for _ in range(10):
    arr *= arr
