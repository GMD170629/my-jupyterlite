picd = {}
numd = {}
fi = open("dir_100.txt",'r')
for stulists in fi:
    stulists = stulists.replace('\n','').split('_') 
    if stulists [0] != '' :
        lkey,lvalue = stulists[1][:-4],eval(stulists [0])
        lval = []
        for v in lvalue:
            if v != '0':
                lval.append(v)
        if lval:
            lv= ','.join(lval)
            print("{}:{}".format( lkey,lv))
            picd[lkey] =lv
fi.close()
idd = {}
for key in picd:
    ids = picd[key].split(',') 
    for num in ids:
        idd[num] = idd.get(num,0) +1
s = 0
for key in idd:
    s += int(idd[key])
count = len(idd)
print("实际参加测试的人数是：",count)
print("人均被测次数是：{:.1f}".format(s/count))