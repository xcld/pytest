## 列表
列表是最基本的数据结构，第一个索引是0（和数组有点类似）
### 列表操作：
> * 索引
> * 切片
> * 追加
> * 删除
> * 长度
> * 切片
> * 循环
> * 包含
### 创建列表
```python
list1 = ['Google', 'Runoob', 1997, 2000]:
```
### list 脚本操作符
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
如下所示：

|Python 表达式|结果|描述|
|:---|:---|:---|
|len([1, 2, 3])|3|长度|
|[1, 2, 3] + [4, 5, 6]|[1, 2, 3, 4, 5, 6]|组合|
|['Hi!'] * 4|['Hi!', 'Hi!', 'Hi!', 'Hi!']|重复|
|3 in [1, 2, 3]|TRUE|元素是否存在于列表中|
|for x in [1, 2, 3]: print x,|1 2 3|迭代|
列表截取：

|Python 表达式|结果|描述|
|:---|:---|:---|
|L[2]|'Taobao'|读取列表中第三个元素|
|L[-2]|'Runoob'|读取列表中倒数第二个元素|
|L[1:]|['Runoob', 'Taobao']|从第二个元素开始截取列表|

### python列表函数和方法
函数：

|序号|函数|
|:---|:---|
|1|len(list)<br>列表元素个数|
|2|max(list)<br>返回列表元素最大值|
|3|min(list)<br>返回列表元素最小值|
|4|list(seq)<br>将元组转换为列表|
### 方法

|序号|方法|
|:---|:---|
|1|list.append(obj)<br>在列表末尾添加新的对象|
|2|list.count(obj)<br>统计某个元素在列表中出现的次数|
|3|list.extend(seq)<br>在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）|
|4|list.index(obj)<br>从列表中找出某个值第一个匹配项的索引位置|
|5|list.insert(index, obj)<br>将对象插入列表|
|6|list.pop([index=-1]])<br>移除列表中的一个元素（默认最后一个元素），并且返回该元素的值|
|7|list.remove(obj)<br>移除列表中某个值的第一个匹配项|
|8|list.reverse()<br>反向列表中元素|
|9|list.sort(cmp=None, key=None, reverse=False)<br>对原列表进行排序|
|10|list.clear()<br>清空列表|
|11|list.copy()<br>复制列表|

```python
class list(object):
    """
    list() -> new empty list
    list(iterable) -> new list initialized from iterable's items
    """
    def append(self, p_object): # real signature unknown; restored from __doc__
        """ L.append(object) -- append object to end """
        pass

    def count(self, value): # real signature unknown; restored from __doc__
        """ L.count(value) -> integer -- return number of occurrences of value """
        return 0

    def extend(self, iterable): # real signature unknown; restored from __doc__
        """ L.extend(iterable) -- extend list by appending elements from the iterable """
        pass

    def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
        """
        L.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        """
        return 0

    def insert(self, index, p_object): # real signature unknown; restored from __doc__
        """ L.insert(index, object) -- insert object before index """
        pass

    def pop(self, index=None): # real signature unknown; restored from __doc__
        """
        L.pop([index]) -> item -- remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.
        """
        pass

    def remove(self, value): # real signature unknown; restored from __doc__
        """
        L.remove(value) -- remove first occurrence of value.
        Raises ValueError if the value is not present.
        """
        pass

    def reverse(self): # real signature unknown; restored from __doc__
        """ L.reverse() -- reverse *IN PLACE* """
        pass

    def sort(self, cmp=None, key=None, reverse=False): # real signature unknown; restored from __doc__
        """
        L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
        cmp(x, y) -> -1, 0, 1
        """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __delslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__delslice__(i, j) <==> del x[i:j]
                   
                   Use of negative indices is not supported.
        """
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

    def __iadd__(self, y): # real signature unknown; restored from __doc__
        """ x.__iadd__(y) <==> x+=y """
        pass

    def __imul__(self, y): # real signature unknown; restored from __doc__
        """ x.__imul__(y) <==> x*=y """
        pass

    def __init__(self, seq=()): # known special case of list.__init__
        """
        list() -> new empty list
        list(iterable) -> new list initialized from iterable's items
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

    def __reversed__(self): # real signature unknown; restored from __doc__
        """ L.__reversed__() -- return a reverse iterator over the list """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __setslice__(self, i, j, y): # real signature unknown; restored from __doc__
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y
                   
                   Use  of negative indices is not supported.
        """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ L.__sizeof__() -- size of L in memory, in bytes """
        pass

    __hash__ = None

list
```