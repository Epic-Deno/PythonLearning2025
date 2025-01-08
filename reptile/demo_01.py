'''
Description: 爬测试页面
Author: zhang zhen
Date: 2025-01-08 16:26:29
LastEditors: zhang zhen
LastEditTime: 2025-01-08 16:34:48
FilePath: /PythonLearning2025/reptile/demo_01.py
'''
import requests

url = "http://127.0.0.1:3000"

dic = {
    "accept-language": "ja,zh;q=0.9",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}

resp = requests.get(url, headers = dic) # 处理头部

# 打印返回信息
print(resp.text)