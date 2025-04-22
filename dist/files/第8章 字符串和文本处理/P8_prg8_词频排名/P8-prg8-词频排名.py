import jieba
fo = open("西游记词汇.txt","r",encoding ="utf-8")
words = fo.readlines() 
fo.close()
sym = "；。，“”： "
DictWords = {}
for ls in words:
    if ls[:-1] not in sym:
        DictWords[ls[:-1]] = DictWords.get(ls[:-1], 0) + 1
        L = list(DictWords.items())
        L.sort(key = lambda s:s[1],reverse=True)
# 输出到文件
fo = open("西游记词频.txt", "w", encoding="utf-8")
for i in range(5):
    fo.writelines(L[i][0] + ":" + str(L[i][1]) + "\n")
fo.close()
# print 输出前5名排名
for i in range(5):
    print(L[i][0] + ":" + str(L[i][1]))
