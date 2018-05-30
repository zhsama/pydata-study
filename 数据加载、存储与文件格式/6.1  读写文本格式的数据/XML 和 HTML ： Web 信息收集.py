# @Version : Python3.6
# @Time    : 2018/5/30 20:53
# @Author  : zhcf1ess
# @Site    : 
# @File    : XML 和 HTML ： Web 信息收集.py
# @Software: PyCharm

import xml
import pandas as pd
import bs4
import hashlib

tables = pd.read_html('fdic_failed_bank_list.html')
# print(len(tables))
failures = tables[0]
# print(failures.head())
close_timestamps = pd.to_datetime(failures['Closing Date'])
print(close_timestamps.dt.year.value_counts())
