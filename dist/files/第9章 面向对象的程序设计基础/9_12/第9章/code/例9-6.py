from wordcloud import WordCloud
import matplotlib.pyplot as plt
words = open(r'C:/case/content.txt',encoding='utf-8').read()
wordcloud = WordCloud(width=1000,height=860,font_path='simhei.ttf')
wordcloud.generate(words)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('C:/case/mywordcloud_1.jpg')