# -*- coding:utf-8 -*-
#动态参数
def func(*args):

    print(args)


# 执行方式一
func(11,33,4,4454,5)

# 执行方式二
li = [11,2,2,3,3,4,54]
func(*li)