# @Version : Python3.6
# @Time    : 2018/6/2 19:03
# @Author  : zhcf1ess
# @Site    : 
# @File    : 排列和随机采样.py
# @Software: PyCharm
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(20).reshape((5, 4)))
print(frame)

sampler = np.random.permutation(5)  # 随机排列
# print(sampler)
# print(frame.take(sampler)) # 按照给定的顺序进行排列 默认轴为axis=0
# print(frame)

# print(frame.sample(n=3, axis=1))
