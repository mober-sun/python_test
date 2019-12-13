"""
斐波那契数列
"""
a , b = 0,1

while b <10:
    print(b,end=",")
    a , b = b,a+b

print("-----------")
"""
条件语句
"""
flag = True
while flag:
    age = int(input("请输入age:"))
    if age <=0:
        print("sb,again")
    elif age >100:
        print("nb,again")
    elif age==26:
        flag = False
        print("yes! you are wonderful")
    elif age >26:
        print("大了")
    else:
        print("小了")

"""
循环语句
"""
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:                            # 只执行一次
    print (count, " 大于或等于 5")
    count = count + 1


sites = ["Baidu", "Google","Runoob","Taobao"]
for x in sites:
    print(x)
else:
    print("no")


"""
range()函数  
如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
range(10);
range(2,7)  指定区间
"""
for x in range(10):
    print(x)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i],end=",")