# @Version : Python3.6
# @Time    : 2018/6/7 19:39
# @Author  : zhcf1ess
# @Site    : 
# @File    : 添加图例.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字符和unicode字符
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum(), 'k', label='one')
ax.plot(np.random.randn(1000).cumsum(), 'k--', label='two')
ax.plot(np.random.randn(1000).cumsum(), 'k.', label='three')
ax.legend(loc='best')
plt.show()
