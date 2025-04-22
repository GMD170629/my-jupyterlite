def fact(n): #声明函数，返回值
    if n==0:
        f=1
    else:
        result=1
        for i in range(1,n+1):
            result*=i
        f=result
    return(f)
n=int(input("请输入整数n（n>=0）："))
print(fact(n))      #调用函数
