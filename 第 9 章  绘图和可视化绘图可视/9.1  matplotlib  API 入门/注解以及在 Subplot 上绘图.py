# @Version : Python3.6
# @Time    : 2018/6/7 19:45
# @Author  : zhcf1ess
# @Site    : 
# @File    : 注解以及在 Subplot 上绘图.py
# @Software: PyCharm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 设置中文字符和unicode字符
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# fig, ax = plt.subplots(1, 1)
# ax.text(0, 0, 'Hello world!', family='monospace', fontsize=10)
# plt.show()

# 图中注射加入特殊符号
fig, ax = plt.subplots(1, 1)

data = pd.read_csv('spx.csv', index_col=0, parse_dates=True)
# print(type(data))
spx = data['SPX']

spx.plot(ax=ax, style='k-')

crisis_data = [
    (datetime(2007, 10, 11), 'Peak of bull market'),
    (datetime(2008, 3, 12), 'Bear Stearns Fails'),
    (datetime(2008, 9, 15), 'Lehman Bankruptcy')
]

for date, label in crisis_data:
    ax.annotate(
        label,
        xy=(date, spx.asof(date) + 75),
        xytext=(date, spx.asof(date) + 225),
        arrowprops=dict(facecolor='black', headwidth=4, width=2, headlength=4),
        horizontalalignment='left',
        verticalalignment='top'
    )

ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])
ax.set_title('Important dates in the 2008-2009 financial crisis')
plt.show()
