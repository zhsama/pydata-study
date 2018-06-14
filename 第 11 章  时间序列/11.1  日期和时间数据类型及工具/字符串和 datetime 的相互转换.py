# @Version : Python3.6
# @Time    : 2018/6/14 17:49
# @Author  : zhcf1ess
# @Site    : 
# @File    : 字符串和 datetime 的相互转换.py
# @Software: PyCharm
from datetime import datetime
from dateutil.parser import parse
import pandas as pd
import numpy as np

# 把时间转换成字符串
stamp = datetime(2011, 1, 3)
# print(stamp)
# print(str(stamp))
# print(stamp.strftime('%Y-%m-%d'))

# 把字符串转换为时间
# value = '2011-01-03'
# print(datetime.strptime(value,'%Y-%m-%d'))

# 传入包含时间字符串的列表
datestrs = ['7/6/2011', '8/6/2011']
# print(datetime.strptime(x, '%y-%m-%d') for x in datestrs)

# dateutil库
# print(parse('7/6/2011'))
# print(parse('7/6/2011', dayfirst=True))

# pandas库
print(pd.to_datetime(datestrs))
# 处理nan
print(pd.to_datetime(datestrs + [None]))
