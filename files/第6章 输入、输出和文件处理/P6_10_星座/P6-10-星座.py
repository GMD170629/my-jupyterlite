#读入CSV格式数据到列表中
fo = open("SunSign.csv","r", encoding='utf-8')
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
fo.close()
while True:
    InputStr = input() # 请输入星座名称,例如双子座
    InputStr.strip()
    flag = False
    if InputStr == 'exit':
        break
    for line in ls:
        if InputStr == line[0]:
            print("{}{}的生日位于{}-{}之间".format(line[0],chr(int(line[3])),line[1],line[2]))
            flag = True
    if flag == False:
        print("输入星座名称有误！")
