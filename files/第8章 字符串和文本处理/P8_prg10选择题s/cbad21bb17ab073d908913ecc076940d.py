import jieba
def qtopic(con):
    conls = jieba.lcut(con)
    #print(conls)
    dict = {}
    for word in conls:
        dict[word] = dict.get(word,0) + 1
    dictls = list(dict.items())
    dictls.sort(key=lambda x: x[1], reverse=True)
    k = 0
    for it in dictls:
        #if it[0] in '的， :：可以是和中或一个以下“”了其时产生ABCD':
        #if it[0] in '的， :：可以是和中或一个以下“”了其时产生ABCD':
        if it[0] in '的,， :：。"“”可以是和中或一个以下了其时产生通过来上':
            continue
        else:
            if k == 3:
                break
            else:
                print('{}:{}'.format(it[0], it[1]))
        k += 1
fi = open("questions.txt", 'r',encoding="utf-8")
con = '' #内容
num1 = 0 #题号
flag = 0
for item in fi:
    item = item.replace('\n', '').strip().split('.')
    try:
        ft = eval(item[0] )   #尝试读取题号
    except:
        pass                  #非题号，则跳过
    else:
        flag += 1     #题号时加1
        num2 = num1   #旧题号
        num1 = ft     #新题号
        if flag > 1:
            print('第 {} 题的主题是： '.format(num2))
            #print(con)
            qtopic(con)
            con = ''
    con += item[1]
print('第 {} 题的主题是： '.format(num1))
qtopic(con)
fi.close()
