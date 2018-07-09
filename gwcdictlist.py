# -*- coding:utf-8 -*-
'''
四、购物车

功能要求：

    要求用户输入总资产，例如：2000
    显示商品列表，让用户根据序号选择商品，加入购物车
    购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
    附加：可充值、某商品移除购物车

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
'''
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
new2 = []
for new in goods:
    new1 =new.values()
    new3 = list(new1)
    new2.append(new3)
for i , a1 in enumerate(new2, 1):
    print(i , a1)
b = int(input("请输入商品编号："))
if b <= len(new2) and b >0:
    print(new2[b - 1])
else:
    print("您输入商品编号有误，请输入正确的商品编号!")