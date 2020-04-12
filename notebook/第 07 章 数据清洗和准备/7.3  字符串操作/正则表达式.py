# @Version : Python3.6
# @Time    : 2018/6/2 19:58
# @Author  : zhcf1ess
# @Site    : 
# @File    : 正则表达式.py
# @Software: PyCharm
import re
import numpy as np
import pandas as pd

text = "foo       bar\t  baz   \tqux"
# print(re.split('\s+', text))

row = re.compile('\s+')
# print(re.split(row, text))

text = """Dave dave@google.com  Steve steve@gmail.com  Rob rob@gmail.com  Ryan ryan@yahoo.com  """
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)
# print(regex.findall(text))
# print(regex.search(text))
# print(regex.search(text).end())
# print(regex.match(text))
# print(regex.sub('REDACTED', text))
