# @Version : Python3.6
# @Time    : 2018/6/14 20:45
# @Author  : zhcf1ess
# @Site    : 
# @File    : WOM 日期.py
# @Software: PyCharm
import pandas as pd
import numpy as np

rng = pd.date_range('2012-01-01', '2012-09-01', freq=' WOM-3FRI')
print(list(rng))