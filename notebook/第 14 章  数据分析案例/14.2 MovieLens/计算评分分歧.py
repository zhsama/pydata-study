# @Version : Python3.6
# @Time    : 2018/9/11 21:34
# @Author  : zhcf1ess
# @File    : 计算评分分歧.py
# @Software: PyCharm

import pandas as pd

pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep="::", header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep="::", header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep="::", header=None, names=mnames)

data = pd.merge(pd.merge(users, ratings), movies)
# print(data)

# 计算平均分
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# print(mean_ratings)

# 获取影评>250的电影
ratings_by_title = data.groupby('title').size()
# print(ratings_by_title)
active_title = ratings_by_title.index[ratings_by_title > 250]
mean_ratings = mean_ratings.loc[active_title]
print(mean_ratings)

# 获取差异最大的影评
mean_ratings['diff'] = mean_ratings['F'] - mean_ratings['M']
sorted_by_diff = mean_ratings.sort_values(by='diff', ascending=False)
# print(sorted_by_diff[:10])

# 查找分歧(按方差/标准差)
ratings_std_by_title = data.groupby('title')['rating'].std()
ratings_std_by_title = ratings_std_by_title.loc[active_title]
print(ratings_std_by_title.sort_values(ascending=False)[:10])

# 根据女性评分降序排列
# top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
# print(top_female_ratings)
