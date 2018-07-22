#-*- encoding: utf8 -*-

'''
列表生成式
'''
def f(n):
    return n**3

#a = [x*x for x in range(10)]
a = [f(x) for x in range(10)]

print(a)
print(type(a))

'''
赋值
相当于a=t[0], b=t[1]
'''
t=('123', 8)
t=['123', 8]
a, b = t
print(a)
print(b)
#t=['123', 8, 9]
#ValueError: too many values to unpack
a, b = t
#a, b, c = t
#ValueError: need more than 2 values to unpack
