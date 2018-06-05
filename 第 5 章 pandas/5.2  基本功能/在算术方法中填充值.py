# @Version : Python3.6
# @Time    : 2018/5/27 20:33
# @Author  : zhcf1ess
# @Site    : 
# @File    : 在算术方法中填充值.py
# @Software: PyCharm

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape(3, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20).reshape(4, 5), columns=list('abcde'))
# print(df1 + df2)
# print(df1.add(df2, fill_value=0))  # 将不重叠的索引对应值设为0

# 带r方法反转参数
print(df1.rsub(df2, fill_value=0))  # 将不重叠的索引对应值设为0 反转参数
print(df1.sub(df2, fill_value=0))  # 将不重叠的索引对应值设为0 反转参数
