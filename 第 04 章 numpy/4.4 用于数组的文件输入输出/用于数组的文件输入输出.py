# @Version : Python3.6
# @Time    : 2018/5/25 21:14
# @Author  : zhcf1ess
# @Site    : 
# @File    : 用于数组的文件输入输出.py
# @Software: PyCharm
import numpy as np

arr = np.arange(10)
# np.save('test', arr)
# print(np.load('test.npy'))
np.savez('array_archive.npz', a=arr, b=arr)
