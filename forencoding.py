# -*- coding:utf-8 -*-
name ="Charles Huang"
zname = "荒杳"
for a in name:
    print(a)
    print( bytes(a, encoding='utf-8'))
for b in zname:
    print(b)
    print( bytes(b, encoding='utf-8'))#输出八进制
    c=bytes(b, encoding='utf-8')
for d in c: #for 循环的元素是字符
    print(d) #默认以十进制输出
    print(d,bin(d))#以二进制输出





