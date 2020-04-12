# @Version : Python3.6
# @Time    : 2018/6/7 20:28
# @Author  : zhcf1ess
# @Site    : 
# @File    : matplotlib 配置配.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('figure', figsize=(10, 10))
font_options = {'family': 'monospace',
                'weight': 'bold',
                'size': 'small'}
plt.rc('font', **font_options)
fig, ax = plt.subplots(1, 1)
plt.show()
