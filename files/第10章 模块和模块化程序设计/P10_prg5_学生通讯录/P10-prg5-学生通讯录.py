def display():
   fi = open("address.csv",'r')
   for stuInfo in fi:
       stuInfo=stuInfo.replace('\n','')   
       print(stuInfo)
   fi.close()        
def insertrec():
   fo = open("address.csv",'a')
   rec = input("请输入要插入的信息，以逗号隔开（示例：103,cc,34567,tianjin）：")
   fo.write(rec)
   fo.write('\n')   
   fo.close()
def deleterec():
   fi = open("address.csv",'r')
   reInfo=[]
   for stuInfo in fi:
       reInfo.append(stuInfo.replace('\n',''))
   fi.close()
   fo = open("address.csv",'w')
   sid = input("请输入要删除的信息（示例：103）：")
   for stuInfo in reInfo:
       if not stuInfo.startswith(sid) :
           fo.write(stuInfo) 
           fo.write('\n')   
   fo.close()
menu=["1. 显示信息","2. 追加信息","3. 删除信息","4. 退出系统"]
flag = 1
while flag:
    for m in menu:
       print(m)
    try:
       ch = int(input("请输入数字1-4选择功能：") )
       flag =1
    except:
       flag = 0
    if ch <1 or ch > 4:
       flag = 1 
    elif ch ==1:
       display()
    elif ch==2:
       insertrec()
    elif ch ==3:
       deleterec()
    elif ch ==4:
       break