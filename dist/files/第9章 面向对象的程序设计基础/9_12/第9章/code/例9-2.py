# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:33:43 2021

@author: lx
"""
import jieba
text = "国庆期间去广州看了小蛮腰，希望有机会登上塔顶。"
jieba.load_userdict("C:/case/dict.txt")
word_list = jieba.cut(text,cut_all=False)
print('/'.join(word_list))