import jieba
fi = open("question.txt",'r',encoding="utf-8")
con = ''
num = 0
for item in fi:
    item = item.replace('\n','').strip().split('.')
    try:
        ft = eval(item[0])
    except:
        pass
    else:
        num = ft 
    con +=item[1]
conls = jieba.lcut(con)
dict = {}
for word in conls:
    dict[word] = dict.get(word, 0) + 1
dictls = list(dict.items())
dictls.sort(key = lambda x:x[1], reverse = True)
k = 0
print('第{}题的主题是：'.format(num) )
for it in dictls:
    if it[0] in '关于的 ,，:：。可以是和中以下':
        continue 
    else:
        if k == 3:
            break 
        else:
            print('{}:{}'.format(it[0],it[1]))
            k += 1
fi.close()
