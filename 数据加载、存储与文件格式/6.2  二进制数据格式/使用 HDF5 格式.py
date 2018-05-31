# @Version : Python3.6
# @Time    : 2018/5/30 21:12
# @Author  : zhcf1ess
# @Site    : 
# @File    : 使用 HDF5 格式.py
# @Software: PyCharm

import pandas as pd
import numpy as np

frame = pd.DataFrame({'a': np.random.randn(1000)})
# print(frame)
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame  # DataFrame对象
store['obj1_col'] = frame['a']  # Series对象
# print(store)
# print(type(store['obj1']))
# print(type(store['obj1_col']))

# store.put('obj2', frame, format='table')  # 将对象存储在HDFStore中
# print(store.select('obj2', where=['index >=  10 and  index <=  15']))
# store.close()

