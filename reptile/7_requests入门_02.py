'''
Description: main description
Author: zhang zhen
Date: 2025-01-09 18:09:56
LastEditors: zhang zhen
LastEditTime: 2025-01-09 18:09:57
FilePath: /PythonLearning2025/reptile/7_requests入门_02.py
'''
'''
Description: Created By Pony
Author: Pony
Date: 2021-10-05 10:36:14
LastEditors: Pony
LastEditTime: 2021-10-05 10:52:11
FilePath: /爬虫/第一章/7_requests入门_02.py
'''
import requests

url = "https://fanyi.baidu.com/sug"

s = input("输入你要查询的单词")

dat = {
    "kw": s
}

# 发送post请求
resp = requests.post(url, data=dat)
print(resp.json()) # 将服务器返回的内容转化成json 
resp.close()  # 关掉
