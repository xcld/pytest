## 字符串
## 常用的功能
* 移除空白
* 分割
* 长度
* 索引
* 切片
## python 转义字符
|转义字符|描述|
|:---|:---|
|\\(在行尾时)|续行符|
|\\\ | 反斜杠符号|
|\\'|单引号|
|\\"|双引号|
|\a|响铃|
|\b|退格(Backspace)|
|\e|转义|
|\000|空|
|\n|换行|
|\v|纵向制表符|
|\t|横向制表符|
|\r|回车|
|\f|换页|
|\oyy|八进制数，yy代表的字符，例如：\o12代表换行|
|\xyy|十六进制数，yy代表的字符，例如：\x0a代表换行|
|\other|其它的字符以普通格式输出|
## python 字符串运算
|运算符	|描述	|示范|
|:----:|:----|:----|
|+|字符串连接|a + b 输出结果： **HelloPython**|
|*|重复输出字符串|a*2 输出结果：**HelloHello**|
|[]|通过索引获取字符串中字符|a[1] 输出结果 **e**|
|[ : ]|截取字符串中的一部分|a[1:4] 输出结果 **ell**|
|in|成员运算符 - 如果字符串中包含给定的字符返回 True|**'H' in a** 输出结果 1|
|not in|成员运算符 - 如果字符串中不包含给定的字符返回 True|**'M' not in a** 输出结果 1|
|r/R|原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。|print( r'\n' )<br> print( R'\n' )|
## Python字符串格式化
### python字符串格式化符号:
|符号|描述|
|:---|:---|
|%c| 格式化字符及其ASCII码|
|%s| 格式化字符串|
|%d| 格式化整数|
|%u| 格式化无符号整型|
|%o| 格式化无符号八进制数|
|%x| 格式化无符号十六进制数|
|%X| 格式化无符号十六进制数（大写）|
|%f| 格式化浮点数字，可指定小数点后的精度|
|%e| 用科学计数法格式化浮点数|
|%E| 作用同%e，用科学计数法格式化浮点数|
|%g| %f和%e的简写|
|%G| %f 和 %E 的简写|
|%p| 用十六进制数格式化变量的地址|
### 格式化操作符辅助指令:
|符号|描述|
|:---|:---|
|*|定义宽度或者小数点精度|
|-|用做左对齐|
|+|在正数前面显示加号( + )|
|\<sp>|在正数前面显示空格|
|#|在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')|
|0|显示的数字前面填充'0'而不是默认的空格|
|%|'%%'输出一个单一的'%'|
|(var)|映射变量(字典参数)|
|m.n.|m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)|
## Python 的字符串内建函数
### Python 的字符串常用内建函数如下：
|序号|方法及描述|
|:---|:---|
|1|capitalize()|
||将字符串的第一个字符转换为大写|
|2|center(width, fillchar)|
||返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。|
|3|count(str, beg= 0,end=len(string))|
||返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数|
|4|bytes.decode(encoding="utf-8", errors="strict")|
||Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。|
|5|encode(encoding='UTF-8',errors='strict')|
||以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'|
|6|endswith(suffix, beg=0, end=len(string))|
||检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.|
|7|expandtabs(tabsize=8)|
||把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。|
|8|find(str, beg=0 end=len(string))|
||检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1|
|9|index(str, beg=0, end=len(string))|
||跟find()方法一样，只不过如果str不在字符串中会报一个异常.|
|10|isalnum()|
||如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False|
|11|isalpha()|
||如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False|
|12|isdigit()|
||如果字符串只包含数字则返回 True 否则返回 False..|
|13|islower()|
||如果字符串中只包含数字字符，则返回 True，否则返回 False|
|15|isspace()|
||如果字符串中只包含空白，则返回 True，否则返回 False.|
|16|istitle()|
||如果字符串是标题化的(见 title())则返回 True，否则返回 False|
|17|isupper()|
||如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False|
|18|join(seq)|
||以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串|
|19|len(string)|
||返回字符串长度|
|20|ljust(width[, fillchar])|
||返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。|
|21|lower()|
||转换字符串中所有大写字符为小写.|
|22|lstrip()|
||截掉字符串左边的空格或指定字符。|
|23|maketrans()|
||创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。|
|24|max(str)|
||返回字符串 str 中最大的字母。|
|25|min(str)|
||返回字符串 str 中最小的字母。|
|26|replace(old, new [, max])|
||把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。|
|27|rfind(str, beg=0,end=len(string))|
||类似于 find()函数，不过是从右边开始查找.|
|28|rindex( str, beg=0, end=len(string))|
||类似于 index()，不过是从右边开始.|
|29|rjust(width,[, fillchar])|
||返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串|
|30|rstrip()|
||删除字符串字符串末尾的空格.|
|31|split(str="", num=string.count(str))|
||num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串|
|32|splitlines([keepends])|
||按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。|
|33|startswith(str, beg=0,end=len(string))|
||检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。|
|34|strip([chars])|
||在字符串上执行 lstrip()和 rstrip()|
|35|swapcase()|
||将字符串中大写转换为小写，小写转换为大写|
|36|title()|
||返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())|
|37|translate(table, deletechars="")|
||根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中|
|38|upper()|
||转换字符串中的小写字母为大写|
|39|zfill (width)|
||返回长度为 width 的字符串，原字符串右对齐，前面填充0|
|40|isdecimal()|
||检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。|


```python
class str(basestring):
    """
    str(object='') -> string
    
    Return a nice string representation of the object.
    If the argument is a string, the return value is the same object.
    """
    def capitalize(self):  
        """ 首字母变大写 """
        """
        S.capitalize() -> string
        
        Return a copy of the string S with only its first character
        capitalized.
        """
        return ""

    def center(self, width, fillchar=None):  
        """ 内容居中，width：总长度；fillchar：空白处填充内容，默认无 """
        """
        S.center(width[, fillchar]) -> string
        
        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None):  
        """ 子序列个数 """
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, encoding=None, errors=None):  
        """ 解码 """
        """
        S.decode([encoding[,errors]]) -> object
        
        Decodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
        as well as any other name registered with codecs.register_error that is
        able to handle UnicodeDecodeErrors.
        """
        return object()

    def encode(self, encoding=None, errors=None):  
        """ 编码，针对unicode """
        """
        S.encode([encoding[,errors]]) -> object
        
        Encodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that is able to handle UnicodeEncodeErrors.
        """
        return object()

    def endswith(self, suffix, start=None, end=None):  
        """ 是否以 xxx 结束 """
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=None):  
        """ 将tab转换成空格，默认一个tab转换成8个空格 """
        """
        S.expandtabs([tabsize]) -> string
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None):  
        """ 寻找子序列位置，如果没找到，返回 -1 """
        """
        S.find(sub [,start [,end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(*args, **kwargs): # known special case of str.format
        """ 字符串格式化，动态参数，将函数式编程时细说 """
        """
        S.format(*args, **kwargs) -> string
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        pass

    def index(self, sub, start=None, end=None):  
        """ 子序列位置，如果没找到，报错 """
        S.index(sub [,start [,end]]) -> int
        
        Like S.find() but raise ValueError when the substring is not found.
        """
        return 0

    def isalnum(self):  
        """ 是否是字母和数字 """
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self):  
        """ 是否是字母 """
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdigit(self):  
        """ 是否是数字 """
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def islower(self):  
        """ 是否小写 """
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isspace(self):  
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self):  
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self):  
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable):  
        """ 连接 """
        """
        S.join(iterable) -> string
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None):  
        """ 内容左对齐，右侧填充 """
        """
        S.ljust(width[, fillchar]) -> string
        
        Return S left-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def lower(self):  
        """ 变小写 """
        """
        S.lower() -> string
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

    def lstrip(self, chars=None):  
        """ 移除左侧空白 """
        """
        S.lstrip([chars]) -> string or unicode
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def partition(self, sep):  
        """ 分割，前，中，后三部分 """
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None):  
        """ 替换 """
        """
        S.replace(old, new[, count]) -> string
        
        Return a copy of string S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None):  
        """
        S.rfind(sub [,start [,end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None):  
        """
        S.rindex(sub [,start [,end]]) -> int
        
        Like S.rfind() but raise ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None):  
        """
        S.rjust(width[, fillchar]) -> string
        
        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def rpartition(self, sep):  
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=None):  
        """
        S.rsplit([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in the string S, using sep as the
        delimiter string, starting at the end of the string and working
        to the front.  If maxsplit is given, at most maxsplit splits are
        done. If sep is not specified or is None, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None):  
        """
        S.rstrip([chars]) -> string or unicode
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def split(self, sep=None, maxsplit=None):  
        """ 分割， maxsplit最多分割几次 """
        """
        S.split([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in the string S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are removed
        from the result.
        """
        return []

    def splitlines(self, keepends=False):  
        """ 根据换行分割 """
        """
        S.splitlines(keepends=False) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None):  
        """ 是否起始 """
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None):  
        """ 移除两段空白 """
        """
        S.strip([chars]) -> string or unicode
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def swapcase(self):  
        """ 大写变小写，小写变大写 """
        """
        S.swapcase() -> string
        
        Return a copy of the string S with uppercase characters
        converted to lowercase and vice versa.
        """
        return ""

    def title(self):  
        """
        S.title() -> string
        
        Return a titlecased version of S, i.e. words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        return ""

    def translate(self, table, deletechars=None):  
        """
        转换，需要先做一个对应表，最后一个表示删除字符集合
        intab = "aeiou"
        outtab = "12345"
        trantab = maketrans(intab, outtab)
        str = "this is string example....wow!!!"
        print str.translate(trantab, 'xm')
        """

        """
        S.translate(table [,deletechars]) -> string
        
        Return a copy of the string S, where all characters occurring
        in the optional argument deletechars are removed, and the
        remaining characters have been mapped through the given
        translation table, which must be a string of length 256 or None.
        If the table argument is None, no translation is applied and
        the operation simply removes the characters in deletechars.
        """
        return ""

    def upper(self):  
        """
        S.upper() -> string
        
        Return a copy of the string S converted to uppercase.
        """
        return ""

    def zfill(self, width):  
        """方法返回指定长度的字符串，原字符串右对齐，前面填充0。"""
        """
        S.zfill(width) -> string
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width.  The string S is never truncated.
        """
        return ""

    def _formatter_field_name_split(self, *args, **kwargs): # real signature unknown
        pass

    def _formatter_parser(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, y):  
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y):  
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y):  
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, format_spec):  
        """
        S.__format__(format_spec) -> string
        
        Return a formatted version of S as described by format_spec.
        """
        return ""

    def __getattribute__(self, name):  
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y):  
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __getslice__(self, i, j):  
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y):  
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y):  
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self):  
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, string=''): # known special case of str.__init__
        """
        str(object='') -> string
        
        Return a nice string representation of the object.
        If the argument is a string, the return value is the same object.
        # (copied from class doc)
        """
        pass

    def __len__(self):  
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y):  
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y):  
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y):  
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, n):  
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more):  
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y):  
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self):  
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmod__(self, y):  
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, n):  
        """ x.__rmul__(n) <==> n*x """
        pass

    def __sizeof__(self):  
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self):  
        """ x.__str__() <==> str(x) """
        pass

```
