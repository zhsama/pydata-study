### 1. 创建Excel文件

```python
# 1. 使用to_excel创建Excel文件
import pandas as pd

df = pd.DataFrame({'id':[1,2,3],'name':['zs','ls','ww']})

# 默认会有索引，将ID列设置成索引,会返回一个新的df,如果想要在原来的df上修改需要添加参数inplace=True
df = df.set_index('id')

df.to_excel('./output.xlsx')
print('end')
```

### 2. 使用pandas读取文件

```python
# 2. 使用pandas读取文件
import pandas as pd
# 此处需要安装依赖库xlrd
people = pd.read_excel('./data/People.xlsx')
# print('获取文件中的行和列：',people.shape)
# print('获取文件中的列名：',people.columns)
# 默认取前五行
# print('获取文件中的前几行数据信息：',people.head())
# print('获取文件中的后几行数据信息：',people.tail())

# 注意常见问题：
# 1. 读取的时候，默认会将第一行作为列名，我们可以修改
# people = pd.read_excel('./data/People1.xlsx',header = 1)
# print(people.columns)

# 2. 如果第一行或者其他行不满足我们的需求时，我们可以自定义
# 第一种： 设置header为None，会使用默认的1234
people = pd.read_excel('./data/People.xlsx',header = None)
# print(people.columns)
# print(people.head())

# 第二种： 认为的设置默认值
# people.columns = ['ID1','Type1','Title1','FirstName1','MiddleName1','LastName1']
# print(people.columns)
# print(people.head())

# 重新存储
# people.set_index('ID1',inplace = True)
# print(people.head())
# people.to_excel('./People1.xlsx')
# print('end')
# 注意读取数据的时候，会将ID1右作为一列输出出来，所以可以在读取的时候用参数指定一下
# people1 = pd.read_excel('./People1.xlsx',index_col = "ID1")
# print(people1.head())

# 指定读哪个表
# sheet = pd.read_excel('./data/sheet.xlsx',sheet_name='sheet2')
# print(sheet.head())

# 3. 如果数据在表格中没有顶格写时
# skiprows : 跳过几行
# usecols: 使用那几列（C,指的就是Excel上的ABCD....）
# book = pd.read_excel('./data/Books.xlsx',skiprows=3,usecols ="C:F")
# print(book.head())
```

### 3. 自动填充内容（数据区域读取填充）

```python
import pandas as pd
book = pd.read_excel('./data/Books.xlsx',skiprows=3,usecols ="C:F")
# print(book['ID'])
# 修改ID 的值
# book["ID"].at[0] = 1
# print(book['ID'])
'''
at和iat函数是只能选择某个位置的值，iat是按照行索引和列索引的位置来选取数据的。而at是按照行索引和列索引来选取数据；
loc和iloc函数的功能包含at和iat函数的功能
'''

# 使用for循环给ID列添加内容
for i in book.index:
    book["ID"].at[i] = i+1
    
# # 注意： 添加后ID由于默认是float类型,修改一下类型
book["ID"]= book["ID"].astype(int)
print(book['ID'])

# # 给inStore添加交替值
# book["InStore"] = book["InStore"].astype(str)
# for i in book.index:
#     book["InStore"].at[i] = 'Yes' if i%2==0 else "No"
    
# book.set_index('ID',inplace=True)
# book.to_excel('./books1.xlsx')
```

### 4. 函数填充计算列(有单价有数量，计算总价格)

```python
import pandas as pd
books = pd.read_excel('./04Books.xlsx',index_col = 'ID')
print(books)

# 计算Price的值(这种方法是列与列之间对齐后进行计算)
books["Price"] = books['OnePrice'] * books['Count']
print(books)

# 如果只想算某一段就可以，使用循环迭代（是单元格与单元格之间的操作）
# for i in range(5,16):
#     books["Price"].at[i] = books["OnePrice"].at[i] * books["Count"].at[i]

# print(books)
# 如果想修改原文件，直接写回去就可以
books.to_excel('./05Books.xlsx')
```

### 5. 排序

```python
import pandas as pd
books = pd.read_excel('./05List.xlsx')
# 将价钱进行排列
'''
by='Price' : 跟据哪一列进行排序
inplace=True ： 是否在原有的DataFrame上修改，
ascending = True ： 默认为升序
'''
# books.sort_values(by='Price',inplace=True,ascending = False)

# 将买过的书按价格高低排列
'''
by=['Buy','Price'] :先排Buy,在这个基础上排Price
ascending = [True,False]: 分别指定buy和price的升降序
'''
books.sort_values(by=['Buy','Price'],inplace=True,ascending = [True,False])
print(books)
```

### 6. 透视表

```python
# 每一个大类的产品每一年的销售总额
import pandas as pd
import numpy as np
orders = pd.read_excel('./data/Orders.xlsx')
# print(orders.head())

# 将插入一列数据年份数据
# print(pd.to_datetime(orders['Date'])[0].year)

orders['Year'] = pd.DatetimeIndex(orders['Date']).year
print(orders.head())

# 制作透视表
pt = orders.pivot_table(index='Category',columns='Year',values = 'Total',aggfunc=np.sum)
print(pt)
```

### 7. Pandas 链接数据库

```python
import pandas as pd
import pymysql

conn =pymysql.connect(host='localhost',user='root',passwd='123',db='tieba',port=3306,charset='utf8mb4')

query = 'SELECT id,info,url FROM tieba_info'

df = pd.read_sql_query(query,conn)
print(df)
```

































