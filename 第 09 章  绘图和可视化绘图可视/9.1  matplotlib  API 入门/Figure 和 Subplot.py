# @Version : Python3.6
# @Time    : 2018/6/5 21:02
# @Author  : zhcf1ess
# @Site    : 
# @File    : Figure 和 Subplot.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()

# 图像应该是 2×2 的（即最多 4 张图），且当前选中的是 4 个 subplot 中的第一个（编号从 1 开始）
ax1 = fig.add_subplot(2, 2, 1)
# plt.plot(np.random.randn(50).cumsum(), 'k--')
ax2 = fig.add_subplot(2, 2, 2)
# plt.plot(np.random.randn(50).cumsum(), '-')
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.show()
# print(type(ax1))

fig, axes = plt.subplots(2, 3)
print(axes)