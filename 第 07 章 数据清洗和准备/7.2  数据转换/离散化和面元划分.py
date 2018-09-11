# @Version : Python3.6
# @Time    : 2018/6/1 21:19
# @Author  : zhcf1ess
# @Site    : 
# @File    : 离散化和面元划分.py
# @Software: PyCharm

import pandas as pd
import numpy as np

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
