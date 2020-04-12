# @Version : Python3.6
# @Time    : 2018/6/9 16:49
# @Author  : zhcf1ess
# @Site    : 
# @File    : 示例：分组加权平均数和相关系数.py
# @Software: PyCharm
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
        'data': np.random.randn(8),
        'weights': np.random.rand(8)
    }
)

grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])  # 计算加权
# print(grouped.apply(get_wavg))

close_px = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)
# print(close_px)
spx_corr = lambda x: x.corrwith(x['SPX'])
rets = close_px.pct_change().dropna()
get_year = lambda x: x.year
by_year = rets.groupby(get_year)
print(by_year.apply(spx_corr))
print(by_year.apply(lambda g: g['AAPL'].corr(g['MSFT'])))
