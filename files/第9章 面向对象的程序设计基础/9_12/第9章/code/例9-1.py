# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:32:43 2021

@author: lx
"""
import jieba
text = "国庆期间去广州看了小蛮腰，希望有机会登上塔顶。"
seg = jieba.cut(text,cut_all=False)
print('精确模式：'+'/'.join(seg))
seg = jieba.lcut(text,cut_all=False)
print(seg)
seg = jieba.cut(text,cut_all=True)
print('全模式：'+'/'.join(seg))
seg = jieba.lcut(text,cut_all=True)
print(seg)
seg = jieba.cut_for_search(text)
print('搜索引擎模式：'+'/'.join(seg))
seg = jieba.lcut_for_search(text)
print(seg)