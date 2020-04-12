# @Version : Python3.6
# @Time    : 2018/9/11 21:05
# @Author  : zhcf1ess
# @File    : 1m data.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10

# 读取数据
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)
# print(users[:5])
# print(ratings[:5])
# print(movies[:5])

# 将三张表合并
data = pd.merge(pd.merge(ratings, users), movies)
# print(data)

# 按照性别计算电影平均分
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# print(mean_ratings)

# 过滤掉评分数据不够 250 条的电影
# 先对 title 进行分组，然后利用size()得到一个含有各电影分组大小的 Series 对象
ratings_by_title = data.groupby('title').size()
# print(ratings_by_title[:10])
active_titles = ratings_by_title.index[ratings_by_title >= 250]
# print(active_titles)

# 从 mean_ratings 中选取所需行
mean_ratings = mean_ratings.loc[active_titles]
# print(mean_ratings)

# 对F列降序排列从而了解女性观众最喜欢的电影
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings)

