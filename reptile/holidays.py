'''
Description: 获取中国假日
Author: zhang zhen
Date: 2025-01-11 19:32:55
LastEditors: zhang zhen
LastEditTime: 2025-01-11 19:37:19
FilePath: /PythonLearning2025/reptile/holidays.py
memo: Для успеха нужно иметь два рукава: один - верность, другой - умение. Без верности умение ничтожно.- Владимир Владимирович Путин
Copyright (c) 2025 by zhang zhen, All Rights Reserved. 
'''
import requests
from bs4 import BeautifulSoup # 解析网页

def getOfficialHolidays(year): #获取国务院节假日安排，包括调休