# @Version : Python3.6
# @Time    : 2018/5/30 21:11
# @Author  : zhcf1ess
# @Site    : 
# @File    : 利用 lxml.objectify 解析 XML.py
# @Software: PyCharm
from lxml import objectify
import pandas as pd
from io  import StringIO

# path = '111.xml'
# parsed = objectify.parse(open(path))
# root = parsed.getroot()
#
# data = []
# skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']
# for elt in root.INDICATOR:
#     el_data = []
#     if __name__ == '__main__':
#         for child in elt.getchildren():
#             if child.tag in skip_fields:
#                 continue
#             el_data[child.tag] = child.pyval
#         el_data.append(el_data)
#
# pref = pd.DataFrame(data)
# print(pref.head())

tag =  '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
# print(root)