# @Version : Python3.6
# @Time    : 2018/6/16 23:59
# @Author  : zhcf1ess
# @Site    : 
# @File    : 为建模创建虚拟变量.py
# @Software: PyCharm
import pandas as pd
import numpy as np

cat_s = pd.Series(['a', 'b', 'c', 'd'] * 2, dtype='category')
print(pd.get_dummies(cat_s))
print(cat_s)