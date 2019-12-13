"""
迭代器和生成器
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：
    iter() # 创建迭代器对象
    next() # 输出迭代器的下一个元素
"""
import sys

list= [1,2,3,4,5,6,7,8,9]
it  = iter(list)

# for x in it:
#     print (x, end=" ")

print("------迭代完了后 不能再迭代出发 再创建迭代器------")

while True:
    try:
        print(next(it),end=",")
    except Exception:
        break



class MyNumbers:
    def __iter__(self):
        self.a = 10
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
print(myiter)
for i in myiter:
    print(i)


