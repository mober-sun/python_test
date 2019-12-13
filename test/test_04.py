"""
字符串格式化

"""
# % 格式字符串
print("my name is %s and age is %d" %('sunhuif',26))


# 三引号 """ python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

# f-string
# f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
name = "sunhuif"
print(f"Hello {name}")  # 替换变量
print(f'{2+4}')         # 6 # 使用表达式

dictionary = {"name":"zhansgan","age":11}
print(dictionary["name"])
print(f'{dictionary["name"]}')

"""
列表
"""
list = ["tom","jerry","mober","sb"]
# 迭代
for x in list:
    print(x)
# 嵌套
list2 = ["jjj",list]
print(list2)
print(list2[1][0])  # tom
# 末尾添加
list2.append(11)
print(list2)
# 排序
print("--------")

l = set()
print(l)