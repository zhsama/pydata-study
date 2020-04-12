# @Version : Python3.6
# @Time    : 2018/6/7 20:18
# @Author  : zhcf1ess
# @Site    : 
# @File    : 将图表保存到文件.py
# @Software: PyCharm
from io import BytesIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fug, ax = plt.subplots(1, 1)
plt.plot(np.random.randn(100).cumsum(), 'k', label='test')
plt.plot(np.random.randn(100).cumsum(), 'k-', label='test')
plt.plot(np.random.randn(100).cumsum(), 'k--', label='test')
plt.legend(loc='best', labels='test')
plt.savefig('figpath.png', dpi=400, bbox_inches='tight')
plt.show()
# 保存到文件类对象
# buffer = BytesIO()
# plt.savefig(buffer)
# plot_data = buffer.getvalue()
