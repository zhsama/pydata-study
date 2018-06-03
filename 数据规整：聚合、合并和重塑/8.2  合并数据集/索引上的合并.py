# @Version : Python3.6
# @Time    : 2018/6/3 19:40
# @Author  : zhcf1ess
# @Site    : 
# @File    : 索引上的合并.py
# @Software: PyCharm
import numpy as np
import pandas as pd

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
# print(left1)
# print(right1)
# 将左侧行索引作为连接键
# print(pd.merge(left1, right1, right_index=True, left_on='key'))
# print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer')) # outer表示求并集

#
lefth = pd.DataFrame({
    'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    'key2': [2000, 2001, 2002, 2001, 2002],
    'data': np.arange(5.)
})
righth = pd.DataFrame(
    np.arange(12).reshape((6, 2)),
    index=[
        ['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
        [2001, 2000, 2000, 2000, 2001, 2002]
    ],
    columns=['event1', 'event2']
)
# print(lefth)
# print(righth)

# 默认多键合并 以列表的形式指明用作合并键的多个列
# print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))
# print(df.index)
# print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer'))  # 外连接 求并集

# 两个dataframe索引均作为连接键
left2 = pd.DataFrame(
    [
        [1., 2.], [3., 4.], [5., 6.]
    ],
    index=['a', 'c', 'e'],
    columns=['Ohio', 'Nevada']
)

right2 = pd.DataFrame(
    [
        [7., 8.], [9., 10.], [11., 12.], [13, 14]
    ],
    index=['b', 'c', 'd', 'e'],
    columns=['Missouri', 'Alabama']
)
# print(pd.merge(left1, right1, left_index=True, right_index=True, how='outer'))

# jion方法
print(left2.join(right2, how='outer'))
print(left1.join(right1, on='key'))
# 传入dataframe对象直接按索引合并
another = pd.DataFrame(
    [
        [7., 8.], [9., 10.], [11., 12.], [16., 17.]
    ],
    index=['a', 'c', 'e', 'f'],
    columns=['New  York', 'Oregon']
)
print(left2.join([right2, another]))
print(left2.join([right2, another], how='outer'))
