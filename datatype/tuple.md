## 元组

Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
### 元组操作
> * 索引
> * 切片
> * 循环
> * 长度
> * 包含
### 创建元组
```python
ages = (11, 22, 33, 44, 55)
ages = tuple((11, 22, 33, 44, 55))
```
### 元组的运算符
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

|Python 表达式|结果|描述|
|:---|:---|:---|
|len((1, 2, 3))|3|计算元素个数|
|(1, 2, 3) + (4, 5, 6)|(1, 2, 3, 4, 5, 6)|连接|
|('Hi!',) * 4|('Hi!', 'Hi!', 'Hi!', 'Hi!')|复制|
|3 in (1, 2, 3)|TRUE|元素是否存在|
|for x in (1, 2, 3): print x,|1 2 3|迭代|
### 元组索引，截取
因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：

|Python 表达式|结果|描述|
|:---|:---|:---|
|L[2]|'SPAM!'|读取第三个元素|
|L[-2]|'Spam'|反向读取，读取倒数第二个元素|
|L[1:]|('Spam', 'SPAM!')|截取元素|
### 元组内置函数

|序号|方法及描述|
|:---|:---|
|1|cmp(tuple1, tuple2)<br>比较两个元组元素。|
|2|len(tuple)<br>计算元组元素个数。|
|3|max(tuple)<br>返回元组中元素最大值。|
|4|min(tuple)<br>返回元组中元素最小值。|
|5|tuple(seq)|

```python
lass tuple(object):
    """
    tuple() -> empty tuple
    tuple(iterable) -> tuple initialized from iterable's items
    
    If the argument is a tuple, the return value is the same object.
    """
    def count(self, value): # real signature unknown; restored from __doc__
        """ T.count(value) -> integer -- return number of occurrences of value """
        return 0

    def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
        """
        T.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        return 0

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
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

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, seq=()): # known special case of tuple.__init__
        """
        tuple() -> empty tuple
        tuple(iterable) -> tuple initialized from iterable's items
        
        If the argument is a tuple, the return value is the same object.
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

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
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

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ T.__sizeof__() -- size of T in memory, in bytes """
        pass
```




