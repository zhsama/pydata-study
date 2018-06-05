# @Version : Python3.6
# @Time    : 2018/5/25 20:19
# @Author  : zhcf1ess
# @Site    : 
# @File    : 用于布尔型数组的方法.py
# @Software: PyCharm

import numpy as np

arr = np.random.randn(100)
print((arr > 0).sum())

bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())
