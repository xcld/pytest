goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]


def chongzhi():
    global zongzichan
    e = int(input("请输入充值金额:"))
    zongzichan = zongzichan + e
    print("充值成功,返回购物车.")
    gouwuche()


def gouwuche():
    global zongzichan
    xiaofei = 0
    print("您选购的商品如下:")
    for c, c1 in enumerate(list, 1):
        for c2, c3 in c1.items():
            xiaofei = xiaofei + c3
            print(c, c2, c3)
    print("总价格:", xiaofei)
    while True:
        d = input("请选择结算(yes) or 前往充值(no):")
        if d == "yes" and zongzichan >= 0:
            print("购买成功,您一共消费了:", xiaofei, "总资产剩余:", zongzichan)
            print("欢迎下次光临,再见.")
            break
        elif d == "yes" and zongzichan < 0:
            d1 = input("购买失败,余额不足,请选择前往充值(yes) or 前往购物车移除商品(no):")
            if d1 == "yes":
                chongzhi()
            elif d1 == "no":
                d2 = int(input("请输入商品编号移除出购物车:"))
                d3 = list[d2 - 1]
                for d4, d5 in d3.items():
                    zongzichan = zongzichan + d5
                    del list[d2 - 1]
                    print("您移除了:", d4, d5)
                    gouwuche()
            else:
                print("指令错误")
        elif d == "no":
            chongzhi()
        else:
            print("指令错误")

    exit()


def shangpin():
    global list
    global zongzichan
    list = []
    while True:
        print("商品编号、名称、价格列表:")
        for keys, a in enumerate(goods, 1):
            a1 = a.get("name")
            a2 = a.get("price")
            print(keys, a1, a2)
        dict = {}
        a3 = int(input("请输入商品编号将其加入购物车:"))
        zongzichan = zongzichan - goods[a3 - 1]["price"]
        a4 = goods[a3 - 1]["name"]
        a5 = goods[a3 - 1]["price"]
        print("商品:", goods[a3 - 1]["name"], "价格:", goods[a3 - 1]["price"], "已加入购物车.")
        dict[a4] = a5
        list.append(dict)
        b = input("请选择继续购物(yes) or 去购物车结算(no):")
        if b == "yes":
            continue
        elif b == "no":
            gouwuche()
        else:
            print("指令错误")


def zichan():
    global zongzichan
    zongzichan = int(input("请输入总资产:"))
    shangpin()


zichan()