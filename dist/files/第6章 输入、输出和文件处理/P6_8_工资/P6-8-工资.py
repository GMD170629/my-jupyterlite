salary = {}
fi = open("data.txt",'r',encoding='utf-8')
for item in fi:
    stud = eval(item )
    sKeyValue = stud.items()
    skey = ''
    svalue = []
    for it in sKeyValue:
        if it[0] =='sid':
            skey = it[1]
        else:
            svalue.append(it[1])
    else:   
        svalue.append(round(sum(svalue)/len(svalue),0))
    salary[skey] = svalue 
fi.close()
so = list(salary.items())
so.sort(key = lambda x:x[0],reverse = False)
for item in so:
    print('{}:{}'.format(item[0],item[1]))
