studs= [{'sid':'103','Chinese': 90,'Math':95,'English':92},{'sid':'101','Chinese': 80,'Math':85,'English':82},{'sid':'102','Chinese': 70,'Math':75,'English':72}]
scores = {}
for stud in studs:
    sv = stud.items()
    v = []
    for it in sv:
        if it[0]=='sid':
            k = it[1]
        else:
            v.append(it[1])
    scores[k]  = v
so = list(scores.items())
so.sort(key = lambda x:x[0],reverse = False)
for stuItem in so:
    print('{}:{}'.format(stuItem[0], stuItem[1]))
