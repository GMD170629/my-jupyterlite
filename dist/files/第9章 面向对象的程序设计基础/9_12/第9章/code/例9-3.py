# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:41:39 2021

@author: lx
"""
from collections import Counter
content=open(r'C:/case/content.txt',encoding='utf-8').read()
print(Counter(content).most_common(5))