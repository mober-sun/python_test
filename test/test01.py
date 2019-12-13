
# 基本语法
'''
print("sdfsdf")
a = 32
print(a)
str = "sunhuifssss"
print(str*3)
if a==31:
    print("yes")
else:
    print("no")
'''

# 关键字
''' 
import keyword
a = keyword.kwlist
print(a)
'''

"""
Number类型
python中数字有四种类型：整数、布尔型、浮点数和复数。
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j

String 类型
python中单引号和双引号使用完全相同。
使用三引号('''或\"\"\")

"""

'''
str = "amazing"
print(str)
# 第一个到倒数第二个
print(str[0:-1])
# 第一个字符
print(str[0])
# 第二个字符到第五个
print(str[2:5])
# 两遍
print(str*2)
# 连接符
print(str+"YES")
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
'''

'''
input("\n\n按下 enter 键后退出。")
'''



x="a"
y="b"
# 换行输出
print( x )
print( y )

print('---------')
# 不换行输出 如果要实现不换行需要在变量末尾加上 end=""
print( x, end=" " )
print( y, end=" " )
print()


"""
import 与 from...import
"""
# 将整个模块(somemodule)导入，格式 为： import somemodule
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print (' \n python 路径为',sys.path)

# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *

from sys import argv,path  #  导入特定的成员

print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path