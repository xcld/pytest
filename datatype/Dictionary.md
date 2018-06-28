## 字典
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
### 字典操作：
> * 索引
> * 新增
> * 删除
> * 键、值、键值对
> * 循环
> * 长度
### 创建字典
```python
person = {"name": "mr.wu", 'age': 18}
person = dict({"name": "mr.wu", 'age': 18})
```
### 字典内置函数和方法

|序号|方法及描述|
|:---|:---|
|1|cmp(dict1, dict2)<br>比较两个字典元素。|
|2|len(dict)<br>计算字典元素个数，即键的总数。|
|3|str(dict)<br>输出字典可打印的字符串表示。|
|4|type(variable)<br>返回输入的变量类型，如果变量是字典就返回字典类型。|
### 内置方法
|序号|方法及描述|
|:---|:---|
|序号|方法及描述|
|1|dict.clear()<br>删除字典内所有元素|
|2|dict.copy()<br>返回一个字典的浅复制|
|3|dict.fromkeys(seq[, val])<br>创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值|
|4|dict.get(key, default=None)<br>返回指定键的值，如果值不在字典中返回default值|
|5|dict.has_key(key)<br>如果键在字典dict里返回true，否则返回false|
|6|dict.items()<br>以列表返回可遍历的(键, 值) 元组数组|
|7|dict.keys()<br>以列表返回一个字典所有的键|
|8|dict.setdefault(key, default=None)<br>和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default|
|9|dict.update(dict2)<br>把字典dict2的键/值对更新到dict里|
|10|dict.values()<br>以列表返回字典中的所有值|
|11|pop(key[,default])<br>删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。|
|12|popitem()<br>随机返回并删除字典中的一对键和值。|
```python
class dict(object):
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    """

    def clear(self): # real signature unknown; restored from __doc__
        """ 清除内容 """
        """ D.clear() -> None.  Remove all items from D. """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ 浅拷贝 """
        """ D.copy() -> a shallow copy of D """
        pass

    @staticmethod # known case
    def fromkeys(S, v=None): # real signature unknown; restored from __doc__
        """
        dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
        v defaults to None.
        """
        pass

    def get(self, k, d=None): # real signature unknown; restored from __doc__
        """ 根据key获取值，d是默认值 """
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def has_key(self, k): # real signature unknown; restored from __doc__
        """ 是否有key """
        """ D.has_key(k) -> True if D has a key k, else False """
        return False

    def items(self): # real signature unknown; restored from __doc__
        """ 所有项的列表形式 """
        """ D.items() -> list of D's (key, value) pairs, as 2-tuples """
        return []

    def iteritems(self): # real signature unknown; restored from __doc__
        """ 项可迭代 """
        """ D.iteritems() -> an iterator over the (key, value) items of D """
        pass

    def iterkeys(self): # real signature unknown; restored from __doc__
        """ key可迭代 """
        """ D.iterkeys() -> an iterator over the keys of D """
        pass

    def itervalues(self): # real signature unknown; restored from __doc__
        """ value可迭代 """
        """ D.itervalues() -> an iterator over the values of D """
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """ 所有的key列表 """
        """ D.keys() -> list of D's keys """
        return []

    def pop(self, k, d=None): # real signature unknown; restored from __doc__
        """ 获取并在字典中移除 """
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """
        pass

    def popitem(self): # real signature unknown; restored from __doc__
        """ 获取并在字典中移除 """
        """
        D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty.
        """
        pass

    def setdefault(self, k, d=None): # real signature unknown; restored from __doc__
        """ 如果key不存在，则创建，如果存在，则返回已存在的值且不修改 """
        """ D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
        pass

    def update(self, E=None, **F): # known special case of dict.update
        """ 更新
            {'name':'alex', 'age': 18000}
            [('name','sbsbsb'),]
        """
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
        If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
        In either case, this is followed by: for k in F: D[k] = F[k]
        """
        pass

    def values(self): # real signature unknown; restored from __doc__
        """ 所有的值 """
        """ D.values() -> list of D's values """
        return []

    def viewitems(self): # real signature unknown; restored from __doc__
        """ 所有项，只是将内容保存至view对象中 """
        """ D.viewitems() -> a set-like object providing a view on D's items """
        pass

    def viewkeys(self): # real signature unknown; restored from __doc__
        """ D.viewkeys() -> a set-like object providing a view on D's keys """
        pass

    def viewvalues(self): # real signature unknown; restored from __doc__
        """ D.viewvalues() -> an object providing a view on D's values """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __contains__(self, k): # real signature unknown; restored from __doc__
        """ D.__contains__(k) -> True if D has a key k, else False """
        return False

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, seq=None, **kwargs): # known special case of dict.__init__
        """
        dict() -> new empty dictionary
        dict(mapping) -> new dictionary initialized from a mapping object's
            (key, value) pairs
        dict(iterable) -> new dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        dict(**kwargs) -> new dictionary initialized with the name=value pairs
            in the keyword argument list.  For example:  dict(one=1, two=2)
        # (copied from class doc)
        """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ D.__sizeof__() -> size of D in memory, in bytes """
        pass

    __hash__ = None

dict
```

