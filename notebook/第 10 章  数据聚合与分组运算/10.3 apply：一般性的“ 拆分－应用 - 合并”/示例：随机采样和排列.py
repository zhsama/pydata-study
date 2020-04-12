# @Version : Python3.6
# @Time    : 2018/6/9 16:48
# @Author  : zhcf1ess
# @Site    : 
# @File    : 示例：随机采样和排列.py
# @Software: PyCharm
import pandas as pd
import numpy as np

suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10] * 3) * 4
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
for suit in ['H', 'S', 'C', 'D']:
    cards.extend(str(num) + suit for num in base_names)

deck = pd.Series(card_val, index=cards)


# print(deck)

#  随机返回五个数
def draw(deck, n=5):
    return deck.sample(n)


# print(draw(deck))
get_suit = lambda card: card[-1]  # 获取缩印的最后一位数
print(deck.groupby(get_suit).apply(draw, n=2))  # 随机返回两个数
print(deck.groupby(get_suit, group_keys=False).apply(draw, n=2)) # 取消index的multiindex对象为dataframe
