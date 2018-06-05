# @Version : Python3.6
# @Time    : 2018/5/31 19:35
# @Author  : zhcf1ess
# @Site    : 
# @File    : api.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
res = requests.get(url)

data = res.json()
# print(data)

issues = pd.DataFrame(data, columns=['number', 'title ', 'labels', 'state '])
# print(issues)
# write = issues.to_csv('ex1.csv')
write = issues.to_excel('ex1.xlsx')