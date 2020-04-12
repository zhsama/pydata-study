# @Version : Python3.6
# @Time    : 2018/5/31 20:12
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import numpy as np
import pandas as pd

# 检测pandasui想中的nan值
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
# print(string_data)
# print(string_data.isnull() )

