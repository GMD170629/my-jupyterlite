import datetime
sName = input("请输入您的姓名：")
birthyear = int(input("请输入您的出生年份："))  #把输入值通过int转换为整型
age = datetime.date.today().year - birthyear
print(sName, age)
