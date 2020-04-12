# @Version : Python3.6
# @Time    : 2018/5/30 19:21
# @Author  : zhcf1ess
# @Site    : 
# @File    : 将数据写出到文本格式.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as ply
import sys

data = pd.read_csv('ex5.csv')
# print(data)
# data.to_csv('out.csv', sep=',')

# data.to_csv(sys.stdout, sep='|', na_rep='NULL')

# data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])

# data.to_csv(sys.stdout, index=False, header=False)

dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
# ts.to_csv('series.csv')
