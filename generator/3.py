#-*- encoding: utf8 -*-

'''
迭代器是一个可迭代对象(Interable)
什么是可迭代对象?(对象拥有iter方法)
l = [1, 2, 3]
l.__iter__()
t = (1, 2, 3)
t.__iter__()
d={'name': '123'}
d.__iter__()
'''
def foo():
    print('ok')
    yield 1
    print('yes')
    yield 2

g = foo()
print('----')

print(type(g))
#print(g)
next(g)
#print(g)
print('----')
#print(next(g))
#print(next(g))


for i in foo():
    print(i)
for i in foo():
    print(i)
