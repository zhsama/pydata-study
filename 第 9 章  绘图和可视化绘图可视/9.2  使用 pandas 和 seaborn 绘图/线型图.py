# @Version : Python3.6
# @Time    : 2018/6/7 20:52
# @Author  : zhcf1ess
# @Site    : 
# @File    : 线型图.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

# 该 Series 对象的索引会被传给 matplotlib，并用以绘制 X 轴
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
# s.plot()
# s.plot(use_index=False)

df = pd.DataFrame(
    np.random.randn(10, 4).cumsum(0),
    columns=['A', 'B', 'C', 'D'],
    index=np.arange(0, 100, 10)
)
df.plot(subplots=True)
plt.show()
