# @Version : Python3.6
# @Time    : 2018/6/9 16:20
# @Author  : zhcf1ess
# @Site    : 
# @File    : 面向列的多函数应用.py
# @Software: PyCharm
import pandas as pd
import numpy as np

tips = pd.read_csv('tips.csv')
# print(tips)
tips['tip_pct'] = tips['tip'] / tips['total_bill']
# print(tips)

# 将函数名以字符串形势传入
grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']
# print(grouped_pct.agg('mean'))

# 传入一组函数名
# print(grouped_pct.agg(['mean', 'std']))

# 传入(name,function)类型的元组
print(grouped_pct.agg([('foo', 'mean'), ('bar', np.std)]))

# 传入函数组成的列表
functions = ['count', 'mean', 'max']
# print(grouped['tip_pct', 'total_bill'].agg(functions))

# 传入字典
# print(grouped.agg({'tip': np.max, 'size': 'sum'}))
# print(grouped.agg({'tip_pct': ['min', 'max', 'mean', 'std'], 'size': 'sum'}))