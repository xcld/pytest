# -*- coding:utf-8 -*-
dic = {
    "广州": {
        "越秀": ["动物园", "区庄", "杨箕"],
        "天河": ["岗顶", "华师", "五山"]
    },
    "河源": {
        "连平": ["高莞", "上坪", "忠信"],
        "龙川": ["老隆", "四都", "黄石"]
    },
    "惠州": {
        "惠城区": ["江北", "下角", "南坛"],
        "惠阳区": ["大亚湾", "淡水", "秋长"]
    }

}
for shi in dic:
    print(shi)
seshi  = input("请输入城市名称:")
for xian in dic[seshi]:
    print(xian)
sexian = input("请输入县（区）名：")
for zhen in dic[seshi][sexian]:
    print(zhen)