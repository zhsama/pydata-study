# @Version : Python3.6
# @Time    : 2018/6/7 15:44
# @Author  : zhcf1ess
# @Site    : 
# @File    : 设置标题、轴标签、刻度以及刻度标签.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字符和unicode字符
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = np.random.randn(1000).cumsum()
fig, axes = plt.subplots(1, 1)
axes.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best', labels='Default')

ticks = axes.set_xticks([0, 250, 500, 750, 1000])
labels = axes.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')
axes.set_xlabel('tag')
axes.set_title('随机漫步')
plt.show()
