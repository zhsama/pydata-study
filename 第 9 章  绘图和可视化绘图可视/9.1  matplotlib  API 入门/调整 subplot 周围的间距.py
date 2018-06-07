# @Version : Python3.6
# @Time    : 2018/6/7 14:42
# @Author  : zhcf1ess
# @Site    : 
# @File    : 调整 subplot 周围的间距.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)  # sharex=True表示共享x轴坐标, sharey=True表示共享y轴坐标
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)  # 创建直方图
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()
