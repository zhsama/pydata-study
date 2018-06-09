# @Version : Python3.6
# @Time    : 2018/6/9 15:56
# @Author  : zhcf1ess
# @Site    : 
# @File    : 根据索引级别分组.py
# @Software: PyCharm
import pandas as pd
import numpy as np

columns = pd.MultiIndex.from_arrays(
    [
        ['US', 'US', 'US', 'JP', 'JP'],
        [1, 3, 5, 1, 3]
    ],
    names=['cty', 'tenor']
)
# print(columns)
hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
# print(hier_df)
print(hier_df.groupby(level='cty', axis=1).count())
