"""
基本数据类型
    变量不声明，必须赋值，赋值后才被创建
"""
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

# 多变量赋予
a, b, c = 1, 2, "runoob"
print( a,b,c)

'''
标准数据类型
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''

# 1、number类型
# 1.1Python3 支持 int、float、bool、complex（复数）。
a1, b1, c1, d1 = 20, 5.5, True, 4+3j
print(type(a1), type(b1), type(c1), type(d1),d1)
# 1.2isinstance  可以判断类型
e1 = 34
print( isinstance(e1,int) )
# 1.3 isinstance 和 type 的区别在于：
    # type()不会认为子类是一种父类类型。
    # isinstance()会认为子类是一种父类类型。

class A:
    AA = 1
    AAs= "SD"

class B(A):
    BB =A.AA   # 父类变量赋值给子类的变量
    Bs = A.AAs

print( isinstance(A(), A) )   #True
print( type(A()) == A )       #True
print( isinstance(B(), A))    #True 子类是父类的一种类型
print( type(B()) == A )       #False
print(B.AA,B.AAs,B.BB,B.Bs)   # 1.4 子类可以调父类的变量

# 1.5 数值运算
print( 7+2)
print( 7-2)
print(3*5)
print(2/8,6/2,7/4)   # 除法 得到浮点数 0.25 3.0 1.75
print(2//8,6//2,7//4) # 除法 得到整数  0 3 1
print(5 % 2) # 取余  1
print(3**4)  # 乘方  81
# 在混合计算时，Python会把整型转换成为浮点数



# 2、String 类型
# 1、Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

# 2、Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print("JJJ\nkeep")
print(r"JJJ\nkeep")
# 注意：
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。***



# 3、List 列表
list = ['abcd',788,2.2,'sad',5555]
tinylist = [123,'wewe']
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print(list[:3])
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

# 3.2 list 元素可以被改变  string 不可以
list[0] = '1111'
list[2:3] = ['222',333]
print(list)     # ['1111', 788, '222', 333, 'sad', 5555]
#list[4:]=[]
print(list)     # ['1111', 788, '222', 333]

print(list[1:4]) # [788,'222', 333]
print(list[1:4:2]) # [788, 333]   索引 1 到索引 4 的位置,间隔索引为2的元素



# 4、Tuple 元组
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组
# string、list 和 tuple 都属于 sequence（序列）。
#
# 注意：
#
#1、与字符串一样，元组的元素不能修改。
#2、元组也可以被索引和切片，方法一样。
#3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
#4、元组也可以使用+操作符进行拼接。



# 5、Set 集合
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if "Rose" in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abcdefg')
b = set('abcd')
print(a-b)   # a 和 b 的差集  {'g', 'e', 'f'}
print(b-a)   # b和a的差集 为  set()
print(a | b) # a 和 b 的并集   {'c', 'd', 'e', 'b', 'a', 'f', 'g'}
print(a & b) # a 和 b 的交集    {'a', 'b', 'd', 'c'}
print(a^b)   # a 和 b 中不同时存在的元素 {'e', 'f', 'g'}
print(b^a)   # b 和 a 中不同时存在的元素 {'e', 'f', 'g'}



# 6、字典 Dictionary
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合
# 键(key)必须使用不可变类型
# 在同一个字典中，键(key)必须是唯一的。  key -value 的形式
dict = {}
tinydict ={'name':'张三', 'age':26}
dict['one'] = 'sdsdsd'
dict[1] = '2222'
print(dict)   # {'one': 'sdsdsd', 1: '2222'}
print(tinydict)
print (tinydict.keys())   # 输出所有键  dict_keys(['name', 'age'])
print (tinydict.values()) # 输出所有值  dict_values(['张三', 26])
# 另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
#
# 注意：
#
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。

"""
python 数据转换

int(x [,base]) 将x转换为一个整数
float(x)        将x转换到一个浮点数
str(x)          将对象 x 转换为字符串
repr(x)   将对象 x 转换为表达式字符串

eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)  将序列 s 转换为一个元组
list(s)   将序列 s 转换为一个列表
set(s)    转换为可变集合 
dict(d)   创建一个字典。d 必须是一个 (key, value)元组序列。
            dict([('Runoob', 1), ('Google', 2)]) or    dict(Runoob=1,Google=2)
            
frozenset(s) 转换为不可变集合

chr(x)    将一个整数转换为一个字符
ord(x)    将一个字符转换为它的整数值
hex(x)    将一个整数转换为一个十六进制字符串
oct(x)    将一个整数转换为一个八进制字符串
"""
#  int(x [,base]) 将x转换为一个整数
st1 = '788'
in1 = int(st1)
print(st1,in1)
print(isinstance(st1,int),isinstance(in1,int))  # False True

