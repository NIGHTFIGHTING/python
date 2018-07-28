#-*- encoding: utf8 -*-

def foo():
    print('ok')
    count = yield 1
    print('yes')
    print(count)
    yield 2

b = foo()
#第一次send前如果没有next,只能传一个send(None)
s = b.send(None) #next(b)
print(s)
s = b.send("ee")
print(s)
