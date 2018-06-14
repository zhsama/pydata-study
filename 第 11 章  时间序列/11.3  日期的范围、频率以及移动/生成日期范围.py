# @Version : Python3.6
# @Time    : 2018/6/14 20:21
# @Author  : zhcf1ess
# @Site    : 
# @File    : 生成日期范围.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from datetime import datetime

index = pd.date_range('2012-04-01', '2012-06-01')
print(index)
