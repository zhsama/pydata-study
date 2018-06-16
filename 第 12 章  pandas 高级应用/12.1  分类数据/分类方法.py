# @Version : Python3.6
# @Time    : 2018/6/16 23:36
# @Author  : zhcf1ess
# @Site    : 
# @File    : 分类方法.py
# @Software: PyCharm
import pandas as pd
import numpy as np

s = pd.Series(['a', 'b', 'c', 'd'] * 2)
cat_s = s.astype('category')
print(cat_s)
print(s)

# print(cat_s.cat.categories) # 获取索引
# print(cat_s.cat.codes)  # 获取值

# 修改categories值
actual_categories = ['a', 'b', 'c', 'd', 'e']
cat_s2 = cat_s.cat.set_categories(actual_categories)

# value_counts()
# print(cat_s.value_counts())
# print(cat_s2.value_counts())

# remove_unused_categories()删除无用类别
cat_s3 = cat_s[cat_s.isin(['a', 'b'])]
# print(cat_s3.cat.remove_unused_categories())
