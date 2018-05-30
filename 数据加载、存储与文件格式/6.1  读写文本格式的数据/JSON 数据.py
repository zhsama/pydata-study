# @Version : Python3.6
# @Time    : 2018/5/30 20:15
# @Author  : zhcf1ess
# @Site    : 
# @File    : JSON 数据.py
# @Software: PyCharm

import json
import pandas as pd

obj = {
    "name": "中国",
    "province": [{
        "name": "黑龙江",
        "cities": {
            "city": ["哈尔滨", "大庆"]
        }
    }, {
        "name": "广东",
        "cities": {
            "city": ["广州", "深圳", "珠海"]
        }
    }, {
        "name": "台湾",
        "cities": {
            "city": ["台北", "高雄"]
        }
    }, {
        "name": "新疆",
        "cities": {
            "city": ["乌鲁木齐"]
        }
    }]
}
result = json.loads(obj)
# print(result)

# 转换成dataframe对象
# asjson = json.dumps(result)
# siblings = pd.DataFrame(result['siblings'], columns=['name', 'cities'])
# print(siblings)

# pandas.read_json
# print(pd.read_json('example.json'))