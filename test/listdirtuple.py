# -*- coding:utf-8 -*-
new=['dk','29n','3sn','ein57','89','d']
new1=list(new)#装入元素
new2=("shi","bu","shi","sha")#定义元组
for a in new:
    print(a)
print(new1)
# for b in new2:
#     print(b)
new3=list(new2)#元组转换成列表
print(new3)
new4={"OS":"Ubuntu","Version":16.04}#定义字典
new5=list(dict.items(new4))#字典转换成列表
print(new5)



