# 从1.csv文件中读取考勤数据
with open("1.csv","r",encoding = "utf-8") as fo:
    foR =fo.readlines() 
ls = []
for line in foR:
    line = line.replace("\n","")
    ls.append(line.split(",") )
# 从name.txt文件中读取所有同学的名单
with open("Name.txt","r",encoding = "utf-8") as foName:
    foNameR = foName.readlines() 
lsAll = []
for line in foNameR:
    line = line.replace("\n","")
    lsAll.append(line)
#求出第一次缺勤同学的名单
    for first in ls:
        if first [0] in lsAll:
            lsAll.remove(first[0])
print("第一次缺勤同学有：",end ="")
for first in lsAll:
    print(first,end=" ")