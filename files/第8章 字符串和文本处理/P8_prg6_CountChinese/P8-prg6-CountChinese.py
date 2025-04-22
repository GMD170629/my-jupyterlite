import jieba
s = input() # 请输入一个中文字符串，包含逗号和句号
s = s.replace("，","").replace("。","")
n = len(s)
k=jieba.lcut(s)
m = len(k)
for i in k:
   print(i, end= "/ ")
print("\n中文词语数为{}。".format(m))
print("中文字符数为{}。".format(n))
