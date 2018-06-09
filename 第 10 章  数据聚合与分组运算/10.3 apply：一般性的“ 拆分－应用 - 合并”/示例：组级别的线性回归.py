# @Version : Python3.6
# @Time    : 2018/6/9 16:48
# @Author  : zhcf1ess
# @Site    : 
# @File    : 示例：组级别的线性回归.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import statsmodels.api  as sm


def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params


close_px = pd.read_csv('stock_px_2.csv', parse_dates=True, index_col=0)
# print(close_px)
spx_corr = lambda x: x.corrwith(x['SPX'])
rets = close_px.pct_change().dropna()
get_year = lambda x: x.year
by_year = rets.groupby(get_year)
print(by_year.apply(regress, 'AAPL', ['SPX']))
