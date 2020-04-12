# @Version : Python3.6
# @Time    : 2018/6/2 19:59
# @Author  : zhcf1ess
# @Site    : 
# @File    : pandas 的矢量化字符串函数.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import re

data = {
    'Dave': 'dave@google.com',
    'Steve': 'steve@gmail.com',
    'Rob': 'rob@gmail.com',
    'Wes': np.nan
}
data = pd.Series(data)
# print(data)
# print(data.isnull())
# print(data.str.contains('gmail'))

# 正则方法
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
print(data.str.findall(pattern, flags=re.IGNORECASE))

matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)
