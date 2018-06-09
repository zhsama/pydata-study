# @Version : Python3.6
# @Time    : 2018/6/9 16:50
# @Author  : zhcf1ess
# @Site    : 
# @File    : 分位数和桶分析.py
# @Software: PyCharm
import pandas as pd
import numpy as np

frame = pd.DataFrame({'data1': np.random.randn(1000), 'data2': np.random.randn(1000)})
# print(frame)
quartiles = pd.cut(frame.data1, 4)


# print(quartiles)

def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}


grouped = frame.data2.groupby(quartiles)
# print(grouped.apply(get_stats).unstack())

grouping = pd.qcut(frame.data1, 10, labels=False)  # 给数据划分范围(10为划分10个区域) label=false表示只显示划分区域编号
# print(grouping)
# grouped = frame.data2.groupby(grouping)
# print(grouped.apply(get_stats).unstack())
