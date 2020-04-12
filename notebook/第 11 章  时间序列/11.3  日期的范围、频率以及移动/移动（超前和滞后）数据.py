# @Version : Python3.6
# @Time    : 2018/6/14 20:47
# @Author  : zhcf1ess
# @Site    : 
# @File    : 移动（超前和滞后）数据.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from datetime import datetime

ts = pd.Series(np.random.randn(4), index=pd.date_range('1/1/2000', periods=4, freq='M'))
print(ts)
print(ts.shift(2))
print(ts.shift(-2))
print(ts.shift(2, freq='M'))
