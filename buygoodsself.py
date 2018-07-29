# -*- coding:utf-8 -*-
mon = int(input("请输入您拥有的资产："))
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
for a,b in enumerate(goods, 1):
    print("商品序号：",a,"商品名称和价格：",list(b.values()))
sum = 0
while 1:
    bh = int(input("请输入商品编号："))
    ym=[]
    if bh <= a and bh >0:
        print(goods[bh - 1])
        ym1 = ym.append(goods[bh - 1].get('name'))
        sum1 = goods[bh - 1].get('price')
        print(sum1)
        print(ym)
        sum += sum
        print(sum)
    # print(a
    else:
        print("您输入商品编号有误，请输入正确的商品编号!")


