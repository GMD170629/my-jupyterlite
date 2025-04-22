filename = input("请输入文件名：\n")
fp = open(filename,"w")
ch = input("请输入字符串：\n")
while ch != '@':
    if '@' in ch:
        t = ch.find("@")
        fp.write(ch[0:t] )
        break 
    else:
        fp.write(ch + " ")
    ch = input("")
fp.close()
