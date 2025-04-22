#求 a 的算术平方根的近似方法
def sqrtA( a ):
    if a<=0:
        return 0
    x0 = a;x1 = (x0 + a / x0) / 2
    while (abs(x1 - x0) > pow(10, -6)):
        x0 = x1; x1 = (x0 + a / x0) / 2
    return x1
#测试代码
a = float(input("请输入x："))
print( a,"的算术平方根=",sqrtA( a ))


