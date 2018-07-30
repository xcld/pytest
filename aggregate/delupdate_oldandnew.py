# -*- coding:utf-8 -*-
old_dict = {
    "#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#2": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#3": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80}
}

# cmdb 新汇报的数据
new_dict = {
    "#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 800},
    "#3": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#4": {'hostname': 'c2', 'cpu_count': 2, 'mem_capicity': 80}
}
old_set = set()
new_set = set()
for old in old_dict:
    old_set.add(old)
    print(old_set)
for new in new_dict:
    new_set.add(new)
    print(new_set)