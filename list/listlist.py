# -*- coding:utf-8 -*-
li =["hai","hao","you","ni","pei","wo"]
egli =["hai","hao","you","ni","pei",{"wo":"charles","you":{"girl":"tong"}}]
print(li)
print(li[2])
print(li[0:2])#前闭后开区间
print(egli)
print(egli[5]["you"]["girl"])
li.append("jiu")
li.append(("hao","hao","kai","xin"))
print(li)
del li[6]
print(li)
print(egli.count("you"))  ##