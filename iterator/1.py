# -*-coding:utf-8-*-
from collections import Iterator, Iterable
#生成器都是迭代器,迭代器不一定是生成器
#list,tuple,dict,string:Iterable(可迭代对象)

l = [1, 2, 3, 5]
d = iter(l)
print(d)
print(isinstance(l, list))
print(isinstance(l, Iterable))
print(isinstance(l, Iterator))
print(isinstance(d, Iterator))

#什没是迭代器?
#条件:1.有iter方法2有next方法

print(next(d))
print(next(d))
print(next(d))
print(next(d))

print("-------------")
#for 循环内部三件事
#1.调用可迭代对象的iter方法,返回一个迭代器对象
#2.不断调用迭代器的next放大
#3.处理StopIteration异常

for i in l:
    print(i)

