# -*- coding:utf-8 -*-
new={"age":18,"name":"charles"}
new1=dict({"from":"China","when":"2018"})
new4=[12,1,4,14,1445,65]
new_dict=dict(enumerate(new4))
new5=new1.get("from")
new6=new1.fromkeys(["d","c","e","f"],[])
new6["d"].append("*")
new3=len(new1)
print(new)
print(new1)
print(new3)
print(new_dict)
print(new5)
print(new6)