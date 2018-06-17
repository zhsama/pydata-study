# @Version : Python3.6
# @Time    : 2018/6/17 20:44
# @Author  : zhcf1ess
# @Site    : 
# @File    : 管道方法.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# a = f(df, arg1=v1)
# b = g(a, v2, arg3=v3)
# c = h(b, arg4=v4)
#
# result = (df.pipe(f, arg1=v1)
#           .pipe(g, v2, arg3=v3)
#           .pipe(h, arg4=v4))
N = 15
times = pd.date_range('2017-05-20  00:00', freq='1min', periods=N)
df = pd.DataFrame({
    'times': times,
    'value': np.arange(N)
})

g = df.groupby(['key1', 'key2'])

df['col1'] = df['col1'] - g.transform('mean')


def group_demean(df, by, cols):
    result = df.copy()
    g = df.groupby(by)
    for c in cols:
        result[c] = df[c] - g[c].transform('mean')
    return result


result = (df[df.col1 < 0].pipe(group_demean, ['key1', 'key2'], ['col1']))
