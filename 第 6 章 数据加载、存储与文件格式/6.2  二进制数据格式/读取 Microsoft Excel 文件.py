# @Version : Python3.6
# @Time    : 2018/5/30 21:12
# @Author  : zhcf1ess
# @Site    : 
# @File    : 读取 Microsoft Excel 文件.py
# @Software: PyCharm

import pandas as pd
import numpy as np

xlsx1 = pd.ExcelFile('ex1.xlsx')
xlsx2 = pd.read_excel(xlsx1, 'Sheet1')
# print(xlsx1)
# print(xlsx2)

frame = pd.read_excel('ex1.xlsx', 'Sheet1')
# print(frame)

excle = pd.ExcelFile('ex2.xlsx')
frame.to_excel(excle, 'Sheet1')
