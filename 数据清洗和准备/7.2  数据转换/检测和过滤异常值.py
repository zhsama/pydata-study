# @Version : Python3.6
# @Time    : 2018/6/1 21:28
# @Author  : zhcf1ess
# @Site    : 
# @File    : 检测和过滤异常值.py
# @Software: PyCharm

import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(1000, 4))
# print(frame)
# print(frame.describe()) # 自动统计
# col = frame['2']
# print(col)
print(frame[2][np.abs(frame[2]) > 3])
