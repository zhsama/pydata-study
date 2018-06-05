# @Version : Python3.6
# @Time    : 2018/5/26 14:50
# @Author  : zhcf1ess
# @Site    : 
# @File    : 伪随机数生成.py
# @Software: PyCharm

import numpy as np

samples = np.random.normal(size=(4, 4, 4))  # 从正态（高斯）分布中抽取随机样本。
# print(samples)

# 全局随机种子
# np.random.seed()

# 局部随机种子
rng = np.random.RandomState(1234)
print(rng.randn(10))
