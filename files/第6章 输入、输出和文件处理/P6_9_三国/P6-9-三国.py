fi=open("三国演义-网络版.txt","r",encoding='utf-8')
fo=open("三国演义-汉字统计.txt","w",encoding='utf-8')
txt=fi.read()
d={}
for c in txt:
    d[c]=d.get(c,0)+1
del d[' ']
del d['\n']
ls=[]
for key in d:
    ls.append("{}:{}".format(key,d[key]))
fo.write(",".join(ls))
fi.close()
fo.close()
