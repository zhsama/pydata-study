# @Version : Python3.6
# @Time    : 2018/5/26 21:26
# @Author  : zhcf1ess
# @Site    : 
# @File    : 重新索引.py
# @Software: PyCharm

import pandas as pd

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

# 根据新索引进行重排。如果某个索引值当前不存在，就引入缺失值
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])  # 创建新对象 重排索引
print(obj2)

#  ffill 可以实现前向值填充
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3.reindex(range(6), method='ffill'))
