## 集合
集合（set）是一个无序不重复元素的序列。创建可以用set（） { }，创建空集合用
set（） 而非{ }（空字典）
### 集合的基本操作
#### 1.添加元素
```python
s.add()
s.update()
```
#### 2.移除元素
删除集合，不存在会报错
```python
s.remove( x )
s.discard( x )
s.pop() #随机删除集合内的元素
```
#### 3.计算元素个数
```python
len(s)
```
#### 4.清空集合
```python
s.clear()
```
```python
class set(object):
    """
    set() -> new empty set object
    set(iterable) -> new set object
     
    Build an unordered collection of unique elements.
    """
    def add(self, *args, **kwargs): # real signature unknown
        """
        Add an element to a set，添加元素
         
        This has no effect if the element is already present.
        """
        pass
 
    def clear(self, *args, **kwargs): # real signature unknown
        """ Remove all elements from this set. 清除内容"""
        pass
 
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a shallow copy of a set. 浅拷贝  """
        pass
 
    def difference(self, *args, **kwargs): # real signature unknown
        """
        Return the difference of two or more sets as a new set. A中存在，B中不存在
         
        (i.e. all elements that are in this set but not the others.)
        """
        pass
 
    def difference_update(self, *args, **kwargs): # real signature unknown
        """ Remove all elements of another set from this set.  从当前集合中删除和B中相同的元素"""
        pass
 
    def discard(self, *args, **kwargs): # real signature unknown
        """
        Remove an element from a set if it is a member.
         
        If the element is not a member, do nothing. 移除指定元素，不存在不保错
        """
        pass
 
    def intersection(self, *args, **kwargs): # real signature unknown
        """
        Return the intersection of two sets as a new set. 交集
         
        (i.e. all elements that are in both sets.)
        """
        pass
 
    def intersection_update(self, *args, **kwargs): # real signature unknown
        """ Update a set with the intersection of itself and another.  取交集并更更新到A中 """
        pass
 
    def isdisjoint(self, *args, **kwargs): # real signature unknown
        """ Return True if two sets have a null intersection.  如果没有交集，返回True，否则返回False"""
        pass
 
    def issubset(self, *args, **kwargs): # real signature unknown
        """ Report whether another set contains this set.  是否是子序列"""
        pass
 
    def issuperset(self, *args, **kwargs): # real signature unknown
        """ Report whether this set contains another set. 是否是父序列"""
        pass
 
    def pop(self, *args, **kwargs): # real signature unknown
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty. 移除元素
        """
        pass
 
    def remove(self, *args, **kwargs): # real signature unknown
        """
        Remove an element from a set; it must be a member.
         
        If the element is not a member, raise a KeyError. 移除指定元素，不存在保错
        """
        pass
 
    def symmetric_difference(self, *args, **kwargs): # real signature unknown
        """
        Return the symmetric difference of two sets as a new set.  对称差集
         
        (i.e. all elements that are in exactly one of the sets.)
        """
        pass
 
    def symmetric_difference_update(self, *args, **kwargs): # real signature unknown
        """ Update a set with the symmetric difference of itself and another. 对称差集，并更新到a中 """
        pass
 
    def union(self, *args, **kwargs): # real signature unknown
        """
        Return the union of sets as a new set.  并集
         
        (i.e. all elements that are in either set.)
        """
        pass
 
    def update(self, *args, **kwargs): # real signature unknown
        """ Update a set with the union of itself and others. 更新 """
        pass
```
