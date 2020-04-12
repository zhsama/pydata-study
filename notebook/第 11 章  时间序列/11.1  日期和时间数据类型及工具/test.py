# @Version : Python3.6
# @Time    : 2018/6/14 16:58
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

now = datetime.now()
# print(now)
# print(now.year, now.month, now.day, now.time())

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
# print(delta)
start = datetime.now()
# add = start + timedelta(12)
less = start - 2 * timedelta(12)
# print(add)
print(less)