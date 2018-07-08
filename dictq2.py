# -*- coding:utf-8 -*-
# li = ["手机", "电脑", '鼠标垫', '游艇']
# # l1=dict.fromkeys(li,enumerate(li,))
# # dir={"d":"y"}
# dir={}
# for k,b in enumerate(li,1):
#     print(k,b)
#     dir[k]=b
# print(dir)
# li2 = len(li)
# ip = int(input('请输入商品序号:'))
# print(dir[ip-1])
# if ak <= len(li):
#     print(dir[ip])
# else:
#     print('输入序号有误，请重新输入')
a = ["手机", "电脑", '鼠标垫', '游艇']
for i , a1 in enumerate(a, 1):
    print(i , a1)
b = int(input("请输入商品编号："))
print(a[b - 1])

