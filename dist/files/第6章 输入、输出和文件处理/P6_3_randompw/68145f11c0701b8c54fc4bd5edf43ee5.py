import random
random.seed(0x1010)  
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890! @#$%^&*"
ls=[]
excludes=" "
while len(ls)< 10:
    pwd=" "
    for i in range(10):
        pwd+=s[random.randint(0,len(s)-1)]
        if pwd[0] in excludes:
           continue
    ls.append(pwd)
    excludes+= pwd[0]
fo=open("随机密码.txt","w")
fo.write("\n".join(ls))
fo.close()