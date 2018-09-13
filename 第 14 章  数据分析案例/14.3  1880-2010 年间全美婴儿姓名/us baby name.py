# @Version : Python3.6
# @Time    : 2018/9/12 19:35
# @Author  : zhcf1ess
# @File    : us baby name.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_rows = 10

# names1880 = pd.read_csv('yob1880.txt', names=['name', 'sex', 'births'])
# print(names1880)
# print(names1880.groupby('sex')['births'].sum())

# 读取数据
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'data/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

# 聚合所有数据
names = pd.concat(pieces, ignore_index=True)
# print(names)

# 对year和sex进行聚合
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)


# print(total_births.tail())

# 图例
# total_births.plot(title='Total births by sex and year')
# plt.show()

def add_prop(group):
    '''
    插入prop列 用于存放指定名字的婴儿数相对于总出生数的比例
    :param group: 需要修改的DataFrame
    :return: 新的DataFrame
    '''
    group['prop'] = group.births / group.births.sum()
    return group


names = names.groupby(['year', 'sex']).apply(add_prop)

# print(names)

# 校验prop比例是否正确
# print(names.groupby(['year', 'sex']).prop.sum())

# 取top1000的数据进行分析
pieces = []
for year, group in names.groupby(['year', 'sex']):
    pieces.append(group.sort_values(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces, ignore_index=True)
# print(top1000)


# 分析命名趋势
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
# print(boys, girls)

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number  of  births   per year")
# plt.show()


# 评估命名多样性的增长
table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
table.plot(
    title='sum of top1000.prop by years and sex',
    yticks=np.linspace(0, 1.2, 13),
    xticks=range(1880, 2020, 10)
)


# plt.show()
# 考虑2010年男孩名字
# df = boys[boys.year == 2010]
# print(df)
# prop_cumsum = df.sort_values(by='prop', ascending=False)['prop'].cumsum()
# print(prop_cumsum[:10])
# 1900年数据
# df = boys[boys.year == 1990]
# prop_cumsum = df.sort_values(by='prop', ascending=False)['prop'].cumsum()
# print(prop_cumsum[:10])

# 对所有 year/sex 组合执行计算
def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().values.searchsorted(q) + 1


diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
# print(diversity.head())
diversity.plot(title="Number of popular names in top 50%")
# plt.show()


# “最后一个字母”的变革
# 对出生数据在年度、性别以及末字母进行聚合
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

table = names.pivot_table('births', index=last_letters,
                          columns=['sex', 'year'], aggfunc=sum)

subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
# print(subtable.head())
# print(subtable.sum())

# 计算最后一个字母占用比例
letter_prop = subtable / subtable.sum()
# print(letter_prop)

# 做出图例
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Mal e')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Fem ale', legend=False)
# plt.show()

# 做出男婴name最后一个字母频率相关时间序列
letter_prop = table / table.sum()
dny_ts = letter_prop.loc[['d', 'n', 'y'], 'M'].T
# print(dny_ns.head())

# 图例
# dny_ts.plot()
# plt.show()


# 变成女孩名字的男孩名字（以及相反的情况)
all_name = pd.Series(top1000.name.unique())
lesley_like = all_name[all_name.str.lower().str.contains('lesl')]
# print(lesley_like)

# 过滤其他的名字，并按名字分组计算出生数以查看相对频率
filtered = top1000[top1000.name.isin(lesley_like)]
# filtered = filtered.groupby('name')['births'].sum()
# print(filtered)

# 按性别和年度进行聚合
table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
# print(table)
table = table.div(table.sum(1), axis=0)
# print(table)

# 绘图
table.plot(style={'M': 'k-', 'F': 'k--'})
plt.show()
