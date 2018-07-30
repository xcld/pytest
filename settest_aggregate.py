# -*- coding:utf-8 -*-
li =set()
l1 = ["je","bk","dd","dd"]
l2 = set(l1)
l = {22,515,151,811,1111,111,11,11,}
k = {11,151,5555,15111,55}
l.add("dii")
print(l2)
print(l)
j = l.difference(k) # 在l存在k不存在的
print(l)
print(j)
k.difference_update(l)
print(l)
print(k)
k = {11,151,5555,15111,55}
se =l.intersection(k) #取交集
print(se)

