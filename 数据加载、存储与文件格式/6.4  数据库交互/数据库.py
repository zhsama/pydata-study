# @Version : Python3.6
# @Time    : 2018/5/31 19:58
# @Author  : zhcf1ess
# @Site    : 
# @File    : shujuku.py
# @Software: PyCharm

import sqlite3
import pandas as pd

query = """  
 CREATE  TABLE  test  
  (a  VARCHAR(20),   b  VARCHAR(20), 
 c  REAL,               d  INTEGER  );"""

con = sqlite3.connect('mydata.sqlite')
# con.execute(query)

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO  test  VALUES(?, ?, ?, ?)"
print(con.executemany(stmt, data))