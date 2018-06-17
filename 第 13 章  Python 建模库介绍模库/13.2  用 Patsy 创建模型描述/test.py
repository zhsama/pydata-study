# @Version : Python3.6
# @Time    : 2018/6/17 22:17
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import patsy

data = pd.DataFrame({
    'x0': [1, 2, 3, 4, 5],
    'x1': [0.01, -0.01, 0.25, -4.1, 0.],
    'y': [-1.5, 0., 3.6, 1.3, -2.]
})
y, x = patsy.dmatrices('y ~  x0 +  x1', data)
# print(y)
# print(x)
# print(np.asarray(y))
# print(np.asarray(x))