# @Version : Python3.6
# @Time    : 2018/9/11 21:34
# @Author  : zhcf1ess
# @File    : 计算评分分歧.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

ratings_by_title = data.groupby('title').size()

active_titles = ratings_by_title.index[ratings_by_title >= 250]

mean_ratings = mean_ratings.loc[active_titles]

top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)

# 找出男性和女性观众分歧最大的电影
# 方案1:给mean_ratings加上一个用于存放平均得分之差的列，并对其进行排序

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')  # 按"diff"排序即可得到分歧最大且女性观众更喜欢的电影
print(sorted_by_diff)
