#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 22:28:53 2018

@author: zehe
"""

# the retio of awardedplayer/player for all schools;
from matplotlib import pyplot as plt 
plt.figure(figsize=(6,9)) #调节图形大小
labels = [u'0',u'1-5',u'6-10',u'10-20',u'20-30',u'30-40',u'40+'] #定义标签
sizes = [47,9,8,29,23,6,8] #每块值
#colors = ['red','yellowgreen','lightskyblue','yellow'] #每块颜色定义
#explode = (0,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      #explode=explode,
                      labels=labels,
                      #colors=colors,
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.show()
