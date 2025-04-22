def fab(n):
    if n <= 2: return(1)
    else:
        return(fab(n-1)+fab(n-2))
n = int(input("请输入>=0的整数："))
for i in range(1,n+1):
    print(format(fab(i),">5"),end=' ')

