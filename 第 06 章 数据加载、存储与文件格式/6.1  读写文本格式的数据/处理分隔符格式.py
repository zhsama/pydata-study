# @Version : Python3.6
# @Time    : 2018/5/30 19:44
# @Author  : zhcf1ess
# @Site    : 
# @File    : 处理分隔符格式.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

f = open('ex7.csv')
reader = csv.reader(f)
# for line in reader:
#     print(line)

# 读取文件到一个多行的列表中
with open('ex7.csv') as f:
    lines = list(csv.reader(f))

header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}  # 转置字典键值


# print(data_dict)

class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


reader = csv.reader(f, dialect=my_dialect)
