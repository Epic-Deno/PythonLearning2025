'''
Description: 获取中国假日
Author: zhang zhen
Date: 2025-01-11 19:32:55
LastEditors: zhang zhen
LastEditTime: 2025-01-11 19:44:18
FilePath: /PythonLearning2025/reptile/holidays.py
memo: Для успеха нужно иметь два рукава: один - верность, другой - умение. Без верности умение ничтожно.- Владимир Владимирович Путин
Copyright (c) 2025 by zhang zhen, All Rights Reserved. 
'''
import requests
from bs4 import BeautifulSoup # 解析网页

def getOfficialHolidays(year): #获取国务院节假日安排，包括调休
    url = "https://www.gov.cn/gongbao/2024/issue_11726/202411/content_6989767.html"  #2025年放假安排url
    rep = requests.get(url)  # Get方式获取网页数据
    rep.encoding = 'utf-8'

    soup = BeautifulSoup(rep.text, 'html.parser')
    pList = soup.find_all('p')
    for item in pList:
        p = item.text
        if '：' in p and '放假' in p: # 找出节假日；
            print(p)

if __name__ == '__main__':
    getOfficialHolidays(2025)