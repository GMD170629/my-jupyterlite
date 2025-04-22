salary = int(input("请输入有固定工资收入的党员的工资基数："))  #月工资基数
if (salary > 0 and salary <= 3000): f = 0.5 / 100 * salary
elif (salary > 3000 and salary <= 5000): f = 1.0 / 100 * salary
elif (salary > 5000 and salary <= 10000): f = 1.5 / 100 * salary
elif (salary > 10000): f = 2.0 / 100 * salary
else: print("月工资基数输入有误！")
print(str.format("月工资基数 = {0}，交纳党费 = {1}", salary, f))

