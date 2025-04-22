##list1=[1,2,3,2,3,4]
##set1=set(list1)
##list1=list(set1)


#list1=[1,2,3,2,3,4]

list1=[]
a=int(input("请输入列表元素（整数，可有重复，-1表示结束输入）：   "))
while(a!=-1):
    list1.append(a)
    a=int(input("请输入列表元素（整数，可有重复，-1表示结束输入）：   "))
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)


