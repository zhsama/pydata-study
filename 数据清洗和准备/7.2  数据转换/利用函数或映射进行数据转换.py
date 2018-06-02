# @Version : Python3.6
# @Time    : 2018/6/1 17:33
# @Author  : zhcf1ess
# @Site    : 
# @File    : 利用函数或映射进行数据转换.py
# @Software: PyCharm

import pandas as pd
import numpy as np

data = pd.DataFrame({'food': ['bacon', 'pulled pork',
                              'bacon', 'Pastrami', 'corned beef',
                              'Bacon', 'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]}
                    )
# print(data)

meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

# lower = data['food'].str.lower()  # 把大写转换成小写
# print(lower)
# data['animals'] = lower.map(meat_to_animal)  # 把字典对象映射到series对象
# print(data)
# exm = lambda x: meat_to_animal[x.lower()]
# print(exm)
# print(data['food'].map())
