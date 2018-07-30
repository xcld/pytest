# -*- coding:utf-8 -*-
'''
二、查找
查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
    li = ["alec", " aric", "Alex", "Tony", "rain"]
    tu = ("alec", " aric", "Alex", "Tony", "rain")
    dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
'''
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' Aric', "k3": "Alex", "k4": "Tony"}

for a in range(len(li)):
    li[a] = li[a].replace(" ", "")
print(li)

tu = list(tu)
for b in range(len(tu)):
    tu[b] = tu[b].replace(" ", "")
tu = tuple(tu)
print(tu)

for c in dic:
    dic[c] = dic[c].replace(" ", "")
print(dic)

for a1 in li:
    if (a1.startswith("a") or a1.startswith("A")) and a1.endswith("c"):
        print(a1)

for b1 in tu:
    if (b1.startswith("a") or b1.startswith("A")) and b1.endswith("c"):
        print(b1)

for c1 in dic:
    c2 = dic[c1].strip()
    if (c2.startswith("a") or c2.startswith("A")) and c2.endswith("c"):
        print(c2)
