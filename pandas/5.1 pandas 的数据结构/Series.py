# @Version : Python3.6
# @Time    : 2018/5/26 17:16
# @Author  : zhcf1ess
# @Site    : 
# @File    : pandas的数据结构.py
# @Software: PyCharm
import pandas as pd

obj = pd.Series([1, 2, 3, 4])
# print(obj)
# print(obj.values)
# print(obj.index)

# obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])  # 自定义索引
# print(obj2)

# 通过字典直接创建series对象
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
# print(obj3)

# 可以传入排好序的字典的键以改变顺序
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(data=sdata, index=states)
# obj4 = pd.Series(states)
# print(obj4)

# 判断缺失值
# print(pd.isnull(obj4))
# print(pd.notnull(obj4))

# 根据运算的索引标签自动对齐数据
# print(obj3 + obj4)

# Series 对象本身及其索引都有一个 name 属性
obj4.name = 'population'
obj4.index.name = 'state'
# print(obj4)

# Series 的索引可以通过赋值的方式就地修改