# @Version : Python3.6
# @Time    : 2018/5/31 17:59
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import pandas as pd
import numpy as np

data = pd.read_csv('ex1.csv')
# print(data)
# data.to_pickle('frame_pickle')
frame = pd.read_pickle('frame_pickle')
# print(frame)

