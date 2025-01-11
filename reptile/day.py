'''
Description: Description
Author: zhang zhen
Date: 2025-01-11 19:45:53
LastEditors: zhang zhen
LastEditTime: 2025-01-11 19:45:59
FilePath: /PythonLearning2025/reptile/day.py
memo: Для успеха нужно иметь два рукава: один - верность, другой - умение. Без верности умение ничтожно.- Владимир Владимирович Путин
Copyright (c) 2025 by zhang zhen, All Rights Reserved.
'''
import datetime

legal_hols = []  # 法定节假日
legal_works = []  # 法定调休上班日期


def getOfficialHolidays(year):  # 获取国务院节假日安排，包括调休
    ...  # 接上面代码
    if '：' in p and '放假' in p:  # 找出节日对应的几行内容
        # print(p)
        holidayStr = p.split("：")[1]
         holidayArranges = holidayStr.split('。')
          for holItem in holidayArranges:
               if '上班' in holItem:  # 调休上班安排
                    workDayStr = holItem.replace('（星期六）', '').replace(
                        '（星期日）', '').replace('上班', '')
                    workDays = workDayStr.split('、')
                    for workDayItem in workDays:
                        workDay = workDayItem.replace(
                            '月', '-').replace('日', '')
                        workDate = datetime.date(year=year, month=int(
                            workDay.split('-')[0]), day=int(workDay.split('-')[1]))
                        legal_works.append(workDate)
                    # print(workDayStr)
                if '放假' in holItem:  # 放假安排
                    dayStr = holItem.split('放假')[0].replace('日', '')
                    # print(dayStr)
                    if '至' in dayStr:
                        dayItems = dayStr.split('至')
                        startDate = dayItems[0]
                        month = int(startDate.split('月')[0])
                        startDay = int(startDate.split('月')[1])
                        endDay = int(dayItems[1])
                        for i in range(startDay, endDay+1):
                            holDate = datetime.date(
                                year=year, month=month, day=i)
                            legal_hols.append(holDate)
                    else:
                        monthDay = dayStr.replace('月', '-')
                        holDate = datetime.date(year=year, month=int(
                            monthDay.split('-')[0]), day=int(monthDay.split('-')[1]))
                        legal_hols.append(holDate)
