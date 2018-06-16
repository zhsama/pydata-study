# @Version : Python3.6
# @Time    : 2018/6/16 22:04
# @Author  : zhcf1ess
# @Site    : 
# @File    : pandas 的分类类型.py
# @Software: PyCharm
import pandas as pd
import numpy as np

fruits = ['apple', 'orange', 'apple', 'apple'] * 2
N = len(fruits)
df = pd.DataFrame(
    {
        'fruit': fruits,
        'basket_id': np.arange(N),
        'count': np.random.randint(3, 15, size=N),
        'weight': np.random.uniform(0, 4, size=N),
    },
    columns=['basket_id', 'fruit', 'count', 'weight']
)
# print(df)
df_cat = df['fruit'].astype('category')
# print(df_cat)
type1 = df_cat.values
# print(type(type1))
# print(type1.categories)
# print(type1.codes)

# 直接创建categorical对象
my_categories = pd.Categorical(['foo', 'bar', 'baz', ' foo', 'bar'])
categories = ['foo', 'bar', 'baz']
codes = [0, 1, 2, 0, 0, 1]
pc = pd.Categorical.from_codes(codes, categories)
# print(pc)

# 创建一个有意义的顺序
ordered_cat = pd.Categorical.from_codes(codes, categories, ordered=True)
print(ordered_cat)

# 排序无序对象
# print(pc.as_ordered())

