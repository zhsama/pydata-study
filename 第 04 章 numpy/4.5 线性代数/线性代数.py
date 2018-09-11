# @Version : Python3.6
# @Time    : 2018/5/26 14:23
# @Author  : zhcf1ess
# @Site    : 
# @File    : 线性代数.py
# @Software: PyCharm
import numpy as np

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
# print(x, y)

# x.dot(y)等价于 np.dot(x, y)
# 既是一个数组方法也是 numpy 命名空间中的一个函数
# print(x.dot(y))
# print(np.dot(x, y))

# print(np.ones(3)) # 创建一维数组
# print(x.dot(np.ones(3)))
# print(x @ np.ones(3))#@符（类似 Python 3.5）也可以用作中缀运算符，进行矩阵乘法

from numpy.linalg import inv, qr

# inv：计算逆矩阵
# qr：
X = np.random.randn(5, 5)
mat = X.T.dot(X)  # 计算 X 和它的转置 X.T 的点积
# print(inv(mat))
# print(mat.dot(inv(mat)))
# q, r = qr(mat)  # 矩阵转换成上三角形式
# print(r)

