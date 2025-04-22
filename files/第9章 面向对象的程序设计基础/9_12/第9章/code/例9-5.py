# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:42:43 2021

@author: lx
"""
import jieba
from wordcloud import WordCloud 
from collections import Counter
import matplotlib.pyplot as plt
words = open(r'C:/case/content.txt',encoding='utf-8').read()
con_words=[x for x in jieba.cut(words) if len(x)>=2]
frequencies=Counter(con_words).most_common()
frequencies=dict(frequencies)
wordcloud = WordCloud(width=1000,height=860,font_path='simhei.ttf')
wordcloud.fit_words(frequencies)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('C:/case/mywordcloud.jpg')