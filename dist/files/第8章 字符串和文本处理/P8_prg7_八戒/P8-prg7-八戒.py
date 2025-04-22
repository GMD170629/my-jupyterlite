import jieba
with open("xiyouji.txt","r",encoding ="utf-8") as f:
    words = f.readlines()
fo = open("西游记词汇.txt","w",encoding ="utf-8")
cishu = 0
for ls in words:
    ls =ls.strip()
    wordlist = list(jieba.cut(ls) )
    for w in wordlist:
        if ("八戒" in w):
            cishu += 1            
    fo.writelines("\n".join(wordlist))
fo.close()
print("“八戒”出现的次数为：",cishu)
