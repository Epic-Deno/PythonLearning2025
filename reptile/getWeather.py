'''
Description: 获取天气的脚本
Author: zhang zhen
Date: 2025-01-13 11:00:48
LastEditors: zhang zhen
LastEditTime: 2025-01-13 11:03:41
FilePath: /PythonLearning2025/reptile/getWeather.py
'''
import requests
from bs4 import BeautifulSoup # 解析网页

def getWeather(): # 获取城市天气
    url = "https://www.weather.com.cn/weather/101190101.shtml" # 南京天气地址