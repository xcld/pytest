# -*- coding:utf-8 -*-
temp =232
t = type(temp) #查看temp类型
print(t)
print(dir(t))#输出类的所有方法
help(t) #查看类的方法
print(temp.bit_length()) #获取temp二进制最短位数
print(dir(str))
a = dir(str)
for b in a:
    print(b)