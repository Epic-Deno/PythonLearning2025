'''
Description: main description
Author: zhang zhen
Date: 2025-01-09 18:08:59
LastEditors: zhang zhen
LastEditTime: 2025-01-09 18:09:00
FilePath: /PythonLearning2025/reptile/4_web请求过程剖析.py
'''
'''
Description: 4_web请求过程剖析
Author: Pony
Date: 2021-10-05 09:15:53
LastEditors: Pony
LastEditTime: 2021-10-05 09:24:17
FilePath: /爬虫/第一章/4_web请求过程剖析.py
'''
# 1.服务器渲染： 在服务器那边直接把数据和HTML合在一起，统一返回给浏览器 
#   在浏览器可以找到数据
# 2.客户端渲染： 
#   第一次请求只要一个html骨架。 
#   第二次请求拿到数据。进行数据展示。
#   在页面源代码中找不到数据

# 熟练使用浏览器抓包