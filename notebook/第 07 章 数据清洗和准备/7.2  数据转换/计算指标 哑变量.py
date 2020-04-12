# @Version : Python3.6
# @Time    : 2018/6/2 19:32
# @Author  : zhcf1ess
# @Site    : 
# @File    : 哑变量.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# frame = pd.DataFrame(
#     np.arange(5 * 4).reshape(5, 4),
#     columns=list('1234'),
#     index=list('abcde')
# )
# print(frame)

# df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
# print(df)
# print(pd.get_dummies(df['key']))
# print(pd.get_dummies(df['key'], prefix='key'))


# mnames = ['movie_id', 'title', 'genres']
# movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)
# print(movies)
# all_genres = []
# for genres in movies['genres']:
#     all_genres.extend(genres.split('|'))
# print(all_genres)
# genre = pd.unique(all_genres)
# print(type(genre))


# np.random.seed(12345)
# values = np.random.rand(10)
# print(values)
# bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
# print(pd.get_dummies(pd.cut(values, bins)))
