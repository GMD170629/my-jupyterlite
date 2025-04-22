# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:44:12 2021

@author: lx
"""
import jieba
from collections import Counter
content=open(r'C:/case/content.txt',encoding='utf-8').read()
con_words=[x for x in jieba.cut(content) if len(x)>=2]
print(Counter(con_words).most_common(5))