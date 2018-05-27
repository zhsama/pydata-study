# @Version : Python3.6
# @Time    : 2018/5/27 20:48
# @Author  : zhcf1ess
# @Site    : 
# @File    : DataFrame 和 Series 之间的运算.py
# @Software: PyCharm

import numpy as np
import pandas as pd

frame = pd.DataFrame(
    np.arange(12).reshape((3, 4)),
    index=list('bde'),
    columns=['Utah', 'Ohio', 'Texas', 'Oregon']
)

# ser = frame.loc['Utah']
# print(frame)
# print(ser)
# print(frame-ser)

ser2 = pd.Series(range(3), index=['Utah', 'Ohio', 'Texas'])  # 匹配行:列标签全部缺失 结果全为nan
ser3 = pd.Series(range(3), index=['b', 'e', 'f'])
# print(frame - ser2)
# print(frame.sub(ser3,axis=0))
# print(frame)
# print(ser2)
print(frame.subtract(ser2, axis=0))
