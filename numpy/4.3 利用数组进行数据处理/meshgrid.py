# @Version : Python3.6
# @Time    : 2018/5/25 16:56
# @Author  : zhcf1ess
# @Site    : 
# @File    : meshgrid.py
# @Software: PyCharm
import numpy as np

points = np.arange(-5, 5, 0.01)
# print(points)
xs, ys = np.meshgrid(points, points)  # 获取座标向量 返回矩阵
# print(xs)
# print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
