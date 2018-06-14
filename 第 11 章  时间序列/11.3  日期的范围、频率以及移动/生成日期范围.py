# @Version : Python3.6
# @Time    : 2018/6/14 20:21
# @Author  : zhcf1ess
# @Site    : 
# @File    : 生成日期范围.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from datetime import datetime

# index = pd.date_range('2012-04-01', '2012-06-01')
# index = pd.date_range('2012-04-01', '2012-06-01', periods=20)
# print(index)
print(pd.date_range('2012-05-02  12:56:31', periods=5))
print(pd.date_range('2012-05-02  12:56:31', periods=5, normalize=True))
