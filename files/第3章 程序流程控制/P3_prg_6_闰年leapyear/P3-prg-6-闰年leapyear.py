import calendar
for y in range (2000,3001):
    #方法一。使用一个逻辑表达式包含所有的闰年条件
    if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        print(y,end=' ')


    #方法二。使用嵌套的if语句，相关语句如下：
    #for y in range (2000,3001):
    #    if (y % 400 == 0): print(y,end=' ')
    #    else:
    #        if (y % 4 == 0):
    #            if (y % 100 != 0): print(y,end=' ')     

    #方法三。使用if-elif语句，相关语句如下：
    #for y in range (2000,3001):
    #    if (y % 400 == 0): print(y,end=' ')
    #    elif (y % 4 != 0): pass
    #    elif (y % 100 != 0): print(y,end=' ')

    #方法四。使用calendar模块的isleap函数来判断闰年，相关语句如下：
    #if (calendar.isleap(y)): print(y,end=' ')
   
