# @Version : Python3.6
# @Time    : 2018/6/2 19:58
# @Author  : zhcf1ess
# @Site    : 
# @File    : 字符串对象方法.py
# @Software: PyCharm
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(16).reshape(4, 4), index=list('abcd'), columns=list('1234'))
# print(df)
val = 'a,b,guido'
# print(val.split(','))

pieces = [x.strip() for x in val.split(',')]
# print(pieces)
first, second, third = pieces
# print(first + '::' + second + '::' + third)
# print('::'.join(pieces))


# print('guido' in val)
# print(val.index(','))
# print(val.find(':'))

print(val.count(','))
print(val.replace(',', '::'))
print(val.replace(',', ''))
