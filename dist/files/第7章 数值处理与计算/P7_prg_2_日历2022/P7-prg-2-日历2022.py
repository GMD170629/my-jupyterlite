import calendar
import locale
textcal = calendar.TextCalendar() #创建文本日历
textcal.pryear(2022)              #打印2022年一年的日历 
loc = locale.getlocale()                               #获取当前系统的locale（本地化配置）
localtextcal = calendar.LocaleTextCalendar(locale=loc) #返回指定locale的月份和星期信息
