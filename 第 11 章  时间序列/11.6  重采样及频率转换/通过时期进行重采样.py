# @Version : Python3.6
# @Time    : 2018/6/15 21:36
# @Author  : zhcf1ess
# @Site    : 
# @File    : 通过时期进行重采样.py
# @Software: PyCharm
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(24, 4),
                     index=pd.period_range('1-2000', '12-2001', freq='M'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio']
                     )
# print(frame[:5])

annual_frame = frame.resample('A-DEC').mean()
# print(annual_frame)

# 升采样
# print(annual_frame.resample('Q-DEC').ffill())
print(annual_frame.resample('Q-DEC', convention='end').ffill())
print(annual_frame.resample('Q-DEC', convention='start').ffill())
# print(annual_frame.resample('Q-MAR').ffill())
