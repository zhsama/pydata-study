# @Version : Python3.6
# @Time    : 2018/5/26 15:09
# @Author  : zhcf1ess
# @Site    : 
# @File    : 随机漫步.py
# @Software: PyCharm
import random
import matplotlib.pyplot as plt
import numpy as np

# random.seed(1313)
# for i in range(100):
#     step = 1 if random.randint(0, 1) else -1
#     print(step)

# position = 0
# walk = [position]
# steps = 1000
# for i in range(steps):
#     step = 1 if random.randint(0, 1) else -1
#     position += step
#     walk.append(position)
# plt.plot(walk[:100])
# plt.show()

# nsteps = 1000
# draws = np.random.randint(0, 2, size=nsteps)  # 从[0,2)返回随机整数。
# print(draws)
# steps = np.where(draws > 0, 1, -1)
# walk = steps.cumsum()  # 求和
# print(walk.max())11
# print(walk.min())

# print((np.abs(walk)>=10).argmax())

# 一次模拟多个随机漫步
# 只要给 numpy.random 的函数传入一个二元元组就可以产生一个二维数组
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nsteps, nwalks))  # size = (col,row)
# print(draws)
steps = np.where(draws > 0, 1, -1)  # 三元判断
walks = steps.cumsum(1)  # 求和
# print(walks.max())
# print(walks.min())
his30 = (np.abs(walks) >= 30).any(1)  # 存在一个》=30的数组
# print(his30.sum())
crossing_times = (np.abs(walks[his30]) >= 30).argmax(1)
print(crossing_times.mean())