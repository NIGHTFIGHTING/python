#-*- coding:utf-8 -*-

a=200

def test1():
    globals()['a'] = 100

def test2():
    print("a=%d"%a)


test1()
test2()

def test3(a):
    print(a)
    a[0] = 200
    print(a)

def test4():
    print("a=%d"%a)


b = [a]

test3(b)
print(b)
test4()
