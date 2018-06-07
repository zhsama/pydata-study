# @Version : Python3.6
# @Time    : 2018/6/7 15:13
# @Author  : zhcf1ess
# @Site    : 
# @File    : 颜色、标记和线型.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# plt.axes.plot(x, y, 'g--')
# plt.axes.plot(x, y, linestyle='--', color='g')
# plt.plot(np.random.randn(30).cumsum(), 'ko--')
# plt.plot(np.random.randn(30).cumsum(),  color='k',  linestyle='dashed', marker= 'o')
# plt.show()

data = np.random.randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
plt.show()