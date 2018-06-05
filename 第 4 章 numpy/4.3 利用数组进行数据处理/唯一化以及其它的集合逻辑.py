# @Version : Python3.6
# @Time    : 2018/5/25 20:55
# @Author  : zhcf1ess
# @Site    : 
# @File    : 唯一化以及其它的集合逻辑.py
# @Software: PyCharm
import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will',
                  'Joe', 'Joe'])
# print(np.unique(names))  # 找出唯一值 返回已排序结果
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
# print(np.unique(ints))

# 测试一个数组中的值在另一个数组中的成员资格
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))  # 返回布尔值
